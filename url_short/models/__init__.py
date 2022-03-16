from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# flake8: noqa
db = SQLAlchemy()
migrate = Migrate()


def init_DB(app):
    db.init_app(app)
    with app.app_context():
        if db.engine.url.drivername == 'sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)
