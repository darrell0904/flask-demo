'''
  Created By FJW in 20181021  
'''
from app.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.spider.yushu_book import YuShuBook
from sqlalchemy import desc, func
from flask import current_app

from app.models import db


from app.view_models.book import BookViewModel

class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
          desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False, Wish.isbn.in_(isbn_list),
                   Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def recent(cls):
        gift_list = Gift.query.filter_by(launched=False).group_by(
          Gift.isbn
          ).order_by(
          desc(Gift.create_time)).limit(
          current_app.config['RECENT_BOOK_PER_PAGE']).distinct().all()
        return gift_list

from app.models.wish import Wish