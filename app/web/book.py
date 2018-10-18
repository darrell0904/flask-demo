from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

@web.route('/book/search')
def search():
	# 原则，有很大可能性为假的条件放在最前面
	# 将耗时的操作放在后面
    q = request.args['q']
    page = request.args['page']

    print('------q------', request)
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)