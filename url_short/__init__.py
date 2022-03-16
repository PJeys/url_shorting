from flask import Flask, request, redirect, jsonify
from url_short.config import Config
from url_short.models import init_DB
from url_short.services.shorting_service import ShortingService


def create_app(test_config=None):
    app = Flask('url_short')

    app.config.from_object(Config())
    if test_config:
        app.config.update(test_config)

    init_DB(app)

    return app


application = create_app()


@application.get("/api/v1/get_short/")
def create_short_url():
    """ Creating short url using ShortingService """
    url = request.args.get('url')
    exp = request.args.get('exp')
    shorted = ShortingService().get_or_create_url(url, exp)
    if shorted == 'exp':
        return jsonify({'message': f'incorrect expire date - {exp}'}), 400
    short_url = f'{shorted.domain}?url={shorted.short_url}'
    return jsonify({'shorted_url': short_url, 'expire_date': shorted.expire_date})


@application.get('/')
def redirect_to_original():
    """ Route to redirect to original url """
    url = request.args.get('url')
    print(url)
    full_url = ShortingService().get_full_url(url)
    print(full_url)
    if not url:
        return jsonify({'message': 'No such url'}), 404
    return redirect(f'{full_url}')

