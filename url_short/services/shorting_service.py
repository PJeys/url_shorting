import datetime
import string
from random import choice
from yaml import safe_load, YAMLError

from url_short.models import db
from url_short.models.models import ShortUrl
from typing import Union


class ShortingService:
    def __init__(self):
        self.domain = self.load_domain()

    @staticmethod
    def is_exists_short(shorted_url: str) -> bool:
        """ Function checks if exist current url in database"""
        u = ShortUrl.query.filter(ShortUrl.short_url == shorted_url).first()
        if u:
            return True
        return False

    @staticmethod
    def load_domain():
        """ Function for loadin domains from config file """
        with open("config/domains.yaml", 'r') as stream:
            try:
                parsed_yaml = safe_load(stream)
                return parsed_yaml
            except YAMLError as exc:
                print(exc)

    def get_or_create_url(self, full_url: str, expire: int, domain: str = None) -> Union[ShortUrl, str]:
        """ Function creates new short url if it is not performed, else returns old one """
        if not expire:
            expire = 90
        if expire < 1 or expire > 365:
            return 'exp'
        if not domain:
            domain = self.domain['default_domain']
        u = ShortUrl.query.filter(ShortUrl.full_url == full_url).first()
        if u:
            return u
        return self.create(full_url, expire, domain)

    def short_url(self) -> str:
        """ Function for creating new unique short url """
        while True:
            url = self.generate_short_id()
            if not self.is_exists_short(url):
                break
        return url

    def create(self, full_url: str, expire: int, domain: str) -> ShortUrl:
        """ Function for creating row with current url in database """
        date_expire = datetime.datetime.now() + datetime.timedelta(days=expire)
        short_url = self.short_url()
        url = ShortUrl(full_url=full_url, short_url=short_url, expire_date=date_expire, domain=domain)
        db.session.add(url)
        db.session.commit()
        return url

    @staticmethod
    def generate_short_id(num_chars: int = 8) -> str:
        """ Function to generate short_url of specified number of characters """
        return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_chars))

    def get_full_url(self, short_url: str) -> Union[str, None]:
        """ Function to get full url from database """
        if self.is_exists_short(short_url):
            return ShortUrl.query.filter(ShortUrl.short_url == short_url).first().full_url
        else:
            return None

    @staticmethod
    def delete_exp_urls():
        """ Function to delete expired urls from database """
        date = datetime.datetime.now()
        exp_urls = ShortUrl.query.filter(ShortUrl.expire_date <= date)
        for url in exp_urls:
            db.session.delete(url)
        db.session.commit()


if __name__ == '__main__':
    pass
