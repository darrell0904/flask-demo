"""
	created by jiawei 
"""

from flask import Flask
from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q, page):
	# 原则，有很大可能性为假的条件放在最前面
	# 将耗时的操作放在后面
	isbn_or_key = is_isbn_or_key(q)
	if isbn_or_key == 'isbn':
		result = YuShuBook.search_by_isbn(q)
	else:
		result = YuShuBook.search_by_keyword(q)

	return jsonify(result)

@app.route('/world')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=app.config['DEBUG'])