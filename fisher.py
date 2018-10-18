"""
	created by jiawei 
"""

from app import create_app

__author = '毛毛'

app = create_app()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=app.config['DEBUG'])