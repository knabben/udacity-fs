from  sqlalchemy import desc
from models import Item, Category
from flask import Blueprint, render_template, session, jsonify
from helpers import get_categories, get_session_string
from schemas import many_category_schema

listing = Blueprint('listing', __name__, template_folder='../templates')


@listing.route("/")
def index():
    categories = get_categories()
    last_items = Item.query.order_by(desc('created_at')).limit(10)

    is_logged, username = False, ''
    if 'username' in session:
        is_logged = True
        username = session['username']

    return render_template('index.html',
                           is_logged=is_logged,
                           username=username,
                           categories=categories,
                           last_items=last_items)


@listing.route("/catalog.json")
def catalog():
    categories = Category.query.all()
    return jsonify(many_category_schema.dump(categories).data)
