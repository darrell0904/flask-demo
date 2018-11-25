'''
  Created By FJW in 20181021  
'''
from app.models.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.spider.yushu_book import YuShuBook
from sqlalchemy import desc
from flask import current_app

from app.view_models.book import BookViewModel

class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

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
