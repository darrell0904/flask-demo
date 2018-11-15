'''
  Created By FJW in 20181021  
'''

from app.libs.classhttp import HTTP
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    # per_page = 15

    def __init__(self):
        self.total = 0,
        self.books = []

    # @classmethod
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']
    
    # @classmethod
    def search_by_keyword(self, keyword, page=1):
        
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        
        self.__fill_collection(result)

    # @staticmethod
    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        print('-----', self.books)
        print('-----', self.total)
        return self.books[0] if self.total >= 1 else None
