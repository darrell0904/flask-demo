from . import web

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from flask import render_template, config, current_app, request, url_for

# def __current_user_status_change():
#     r = request


@web.route('/')
# @cache.cached(timeout=100, unless=__current_user_status_change)
# @cache.cached(timeout=100)
def index():
    gift_lists = Gift.recent()
    print('-----gift_lists---', gift_lists)
    books = [BookViewModel(gift.book) for gift in gift_lists]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    pass


