'''
  Created By FJW in 20181021  
'''
from app.view_models.trade import TradeInfo
from flask import jsonify, request, render_template
from app.forms.book import SearchForm
from flask_login import current_user

import json

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection, BookViewModel

from app.models.gift import Gift
from app.models.wish import Wish

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

        # return json.dumps(books, default = lambda x: x.__dict__)
        # return jsonify(result)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):

    has_in_gifts = False
    has_in_wishes = False

     # 获取图书信息
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])

    if current_user.is_authenticated:
        # 如果未登录，current_user将是一个匿名用户对象
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    # if has_in_gifts:
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    print('---trade_wishes_model---', trade_wishes_model)

    return render_template('book_detail.html',book=book, has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes, wishes=trade_wishes_model, gifts=trade_gifts_model)