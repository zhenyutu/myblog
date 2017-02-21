from flask_wtf import FlaskForm
from flask_pagedown.fields import PageDownField
from wtforms import StringField, SubmitField,TextAreaField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):
    markDownEdit = PageDownField('markDownEdit')
    title = StringField('title', validators=[Required()])
    category = SelectField('category', validators=[Required()])
    tag = StringField('tag', validators=[Required()])
    describe = TextAreaField('describe', validators=[Required()])
    submit = SubmitField('Submit')
