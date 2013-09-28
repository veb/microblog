from wtforms import Form, TextField, BooleanField, TextField, BooleanField, TextAreaField, validators

class EditForm(Form):
    nickname = TextField('nickname', [validators.Required()])
    about_me = TextAreaField('about_me', [validators.Length(min = 0, max = 140)])

class LoginForm(Form):
    openid = TextField('openid', [validators.Required()])
    remember_me = BooleanField('remember_me', default = False)
