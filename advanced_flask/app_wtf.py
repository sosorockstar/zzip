from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import length, Required, EqualTo

class RegistrationForm(Form):
    name = TextField('Username', [length(min=4, max=25)])
    email = TextField('Email Address', [length(min=6, max=35)])
    password = PasswordField('New Password', [
        Required(), EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

from flask import Flask, render_template, request
from flask_wtf.csrf import CsrfProtect

from ext import db
from users import User