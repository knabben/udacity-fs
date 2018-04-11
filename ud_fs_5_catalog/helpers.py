import random
import string
from functools import wraps
from flask import flash, redirect, session
from models import db, Category


def redirect_flash(msg, status=None):
    flash(msg, status)
    return redirect('/')


def create_db(app):
    db.create_all(app=app)


def get_categories():
    return Category.query.all()


def get_session_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for x in xrange(32))


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect_flash('User not logged in.', 'error')
        else:
            return func(*args, **kwargs)
    return wrapper

