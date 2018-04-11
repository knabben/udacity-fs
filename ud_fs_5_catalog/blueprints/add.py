from models import Item, Category, db
from helpers import get_categories, redirect_flash, logged
from flask import Blueprint, render_template, session, request


add = Blueprint('add', __name__, template_folder='../templates')


@add.route("/item", methods=['GET', 'POST'])
@logged
def add_item():
    categories = get_categories()
    if not categories:
        return redirect_flash('No categories, add one first.', status='error')

    if request.method == 'GET':
        return render_template('add_item.html', categories=categories)

    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = request.form['category']

        if all([name, description, category]):  # is valid form
            item = Item(name=name, description=description, category_id=category)

            db.session.add(item)
            db.session.commit()

            return redirect_flash('Successfully updated item name')

        else:
            return redirect_flash('Wrong fields editing item.', status='error')



@add.route("/category", methods=['GET', 'POST'])
@logged
def add_category():
    if request.method == 'GET':
        return render_template('add_category.html')

    elif request.method == 'POST':
        name = request.form['name']

        if all([name]):  # is valid form
            category = Category(name=name, user_id=session['user_id'])

            db.session.add(category)
            db.session.commit()

            return redirect_flash('Successfully updated item name')

        else:
            return redirect_flash('Wrong fields editing item.', status='error')
