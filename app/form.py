from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import Required

class PostForm(FlaskForm):
    markDownEdit = PageDownField('markDownEdit')
    title = StringField('title', validators=[Required()])
    category = StringField('category', validators=[Required()])
    tag = StringField('tag', validators=[Required()])
    submit = SubmitField('Submit')
