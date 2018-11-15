'''
  Created By FJW in 20181021  
'''
from flask import render_template
from flask import request, flash, url_for
from app.forms.auth import RegisterForm
from . import web

@web.route('/register')
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    pass


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass


@web.route('/register/confirm/<token>')
def confirm(token):
    pass


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass


