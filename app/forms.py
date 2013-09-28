from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
from flask.ext.wtf import validators, Required, Length

class EditForm(Form):
    nickname = TextField('nickname', [validators.Required()])
    about_me = TextAreaField('about_me', [validators.Length(min = 0, max = 140)])

class LoginForm(Form):
    openid = TextField('openid', [validators.Required()])
    remember_me = BooleanField('remember_me', default = False)
