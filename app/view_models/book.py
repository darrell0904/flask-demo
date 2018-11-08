'''
  Created By FJW in 20181021  
'''

class BookViewModel:
    def __init__(self, data):
        # print('--BookViewModel-data-', data)
        self.title = data['title']
        self.author = '、'.join(data['author'])
        self.publisher = data['publisher']
        self.image = data['image']
        self.pubdate = data['pubdate']
        self.summary = data['summary']
        self.pages = data['pages']

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        # print('-----yushu_book-----', yushu_book)
        # print('-----keyword-----', keyword)

        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned
    
    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books':[],
            'total':0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    # 切割数据
    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'author': '、'.join(data['author']),
            'publisher': data['publisher'],
            'image': data['image'],
            'price': data['price'],
            'summary': data['summary'] or '',
            'pages': data['pages'] or ''
        }
        return book
