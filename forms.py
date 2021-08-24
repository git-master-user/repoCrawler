from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired, Optional


class UserInput(FlaskForm):
    github_user_name = StringField(validators=[DataRequired()], render_kw={'placeholder': 'git user name'})
    programing_language = StringField('programing language', validators=[Optional()])
    min_num_of_stars = IntegerField(validators=[DataRequired()], render_kw={'placeholder': 'Num of stars'})
    submit_data = SubmitField('Send Data')

