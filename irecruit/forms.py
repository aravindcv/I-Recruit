from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from irecruit.models import Admin, User, Skill

class AdminloginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class DetailsForm(FlaskForm):
    firstname = StringField('Firstname',
                           validators=[DataRequired()])
    lastname = StringField('Lastname',
                           validators=[DataRequired()])
    dob = DateField('Date of Birth', format='%d/%m/%Y')
    skill1 = StringField('Skill_1',
                           validators=[DataRequired()])
    skill2 = StringField('Skill_2')
    skill3 = StringField('Skill_3')
    skill4 = StringField('Skill_4')
    level1 = SelectField(
        'Level1',
        choices=[('beg', 'Beginner'), ('int', 'Intermediate'), ('adv', 'Advanced')])
    level2 = SelectField(
        'Level2',
        choices=[('beg', 'Beginner'), ('int', 'Intermediate'), ('adv', 'Advanced')])
    level3 = SelectField(
        'Level3',
        choices=[('beg', 'Beginner'), ('int', 'Intermediate'), ('adv', 'Advanced')])
    level4 = SelectField(
        'Level4',
        choices=[('beg', 'Beginner'), ('int', 'Intermediate'), ('adv', 'Advanced')])
    submit = SubmitField('Submit')
