from flask import jsonify, request
from app.forms.book import SearchForm

import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection

from . import web

@web.route('/book/search')
def search():
	# 原则，有很大可能性为假的条件放在最前面
	# 将耗时的操作放在后面
    q = request.args['q']
    page = request.args['page']

    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = YuShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            
            yushu_book.search_by_keyword(q, page)
            # result = YuShuBook.search_by_keyword(q)
            # result = BookViewModel.package_collection(result, q)

        books.fill(yushu_book, q)

        return json.dumps(books, default = lambda x: x.__dict__)
        # return jsonify(result)
    else:
        return jsonify(form.errors)