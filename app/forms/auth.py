from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email

class RegisterForm(Form):
    email = StringField(validators=[DataRequired(), Length(8, 64),
                                            Email(message='电子邮箱不符合规范')])

    nickname = StringField(validators=[
        DataRequired(), Length(2, 10, message='昵称至少需要两个字符，最多10个字符')])

    password = PasswordField(validators=[
        DataRequired(), Length(6, 32)])

