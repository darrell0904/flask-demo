'''
  Created By FJW in 20181021  
'''

from . import web

@web.route('/my/gifts')
def my_gifts():
    pass

@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass

