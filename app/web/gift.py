'''
  Created By FJW in 20181021  
'''
from flask import render_template, flash, request, redirect, url_for, current_app

from . import web
from flask_login import login_required, current_user

from app.models.gift import Gift
from app.view_models.trade import MyTrades
from app.models import db

@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)
    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    print('--isbn--', isbn)
    if current_user.can_save_to_list(isbn):
        # 既不在赠送清单，也不在心愿清单才能添加
        with db.auto_commit():
            gift = Gift()
            gift.uid = current_user.id
            gift.isbn = isbn
            # gift.book_id = yushu_book.data.id
            db.session.add(gift)
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))

