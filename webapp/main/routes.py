from flask import Blueprint, render_template, request, url_for, flash, redirect, request, abort, current_app
from webapp.main.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
# import webapp.main.utils as utils
import datetime

main = Blueprint('main', __name__)

# Static pages
@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Dynamic pages
@main.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.firstname.data)
        print(form.password.data)
        print(form.email.data)
        print(form.password.data)
        return redirect(url_for("main.register"))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        return redirect(url_for('main.home'))
    return render_template('login.html', form=form)
