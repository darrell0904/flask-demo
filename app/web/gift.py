'''
  Created By FJW in 20181021  
'''

from . import web
from flask_login import login_required, current_user

from app.models.gift import Gift

@web.route('/my/gifts')
@login_required
def my_gifts():
    pass

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    gift = Gift()
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    gift.isbn = isbn
    db.session.add(gift)
    db.session.commit()
    pass

