from classhttp import HTTP

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        print('------isbn', isbn)
        url = cls.isbn_url.format(isbn)
        print('------url', url)
        result = HTTP.get(url)
        return result
    
    @classmethod
    def search_by_keyword(self, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        result = HTTP.get(url)
        return result