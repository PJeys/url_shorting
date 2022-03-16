from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, Column, Integer, String, DateTime
from url_short.models import db


class ShortUrl(db.Model):
    __tablename__ = 'urls'
    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('short_url', 'domain'),
    )
    id = Column(Integer, autoincrement=True)
    full_url = Column(String(500))
    short_url = Column(String(30))
    domain = Column(String(40))
    expire_date = Column(DateTime)
