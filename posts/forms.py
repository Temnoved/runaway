from wtforms import Form
from wtforms import StringField
from wtforms import TextAreaField


class PostForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
