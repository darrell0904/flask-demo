from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1, max=30,message='收件人姓名长度必须在1到30个字符之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
