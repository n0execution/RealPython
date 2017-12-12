from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email



class RegisterForm(Form) :
    name = StringField('Username', 
                        validators=[DataRequired(), Length(min = 6, max = 25)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email(), Length(min = 6, max = 40)])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min = 6, max = 40)])
    confirm = PasswordField('Repeat Password', 
                            validators=[DataRequired(), 
                                    EqualTo('password', message = 'Passwords do not match')])



class LoginForm(Form) :
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
