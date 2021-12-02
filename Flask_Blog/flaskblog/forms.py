from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import length, DataRequired, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username= StringField('username',
        validators=[DataRequired(),length(min=2, max=20) ])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('password', validators=[DataRequired() ])
    confirm_password=PasswordField('confirm password',
        validators=[DataRequired(),EqualTo('password') ])

    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username= username.data).first()
        if user:
            raise ValidationError("Username Taken")

    def validate_email(self,email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError("email Taken")


class LoginForm(FlaskForm):
    # username= StringField('username',
    #     validators=[DataRequired(),length(min=2, max=20) ])
    email  = StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('password', validators=[DataRequired() ])
    remember =BooleanField("Remember Me")
    # confirm_password=PasswordField('pass',
    #     validators=[DataRequired(),EqualTo('password') ])
    submit=SubmitField('Login')




