from models import Item, Category
from flask import Blueprint, render_template, session
from helpers import get_categories

detail = Blueprint('detail', __name__, template_folder='../templates')


@detail.route("/category/<category_name>")
def categories(category_name):
    is_logged, username = False, ''
    if 'username' in session:
        is_logged = True
        username = session['username']

    categories = get_categories()
    category = Category.query.filter_by(name=category_name).first()

    items = category.items
    items_count = len(items)

    return render_template('category.html',
                           category_name=category_name,
                           categories=categories,
                           items_count=items_count,
                           is_logged=is_logged,
                           username=username,
                           items=items)


@detail.route("/item/<item_name>")
def item(item_name):
    is_logged, username = False, ''
    if 'username' in session:
        is_logged = True
        username = session['username']

    item = Item.query.filter_by(name=item_name).first()
    return render_template('item.html',
                           item=item,
                           is_logged=is_logged,
                           username=username)
