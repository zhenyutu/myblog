from flask.ext.wtf import Form
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import Required

class PostForm(Form):
    title = StringField('title', validators=[Required()])
    category = StringField('category', validators=[Required()])
    tag = StringField('tag', validators=[Required()])
    markDownEdit = TextAreaField('markDownEdit', validators=[Required()])
    submit = SubmitField('Submit')
