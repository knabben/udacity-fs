from models import db, Item, Category
from flask import Blueprint, render_template, session, request
from helpers import redirect_flash, logged


edit = Blueprint('edit', __name__, template_folder='../templates')


@edit.route("/item/<item_name>", methods=['GET', 'POST'])
@logged
def edit_item(item_name):
    """ Edit item """
    item = Item.query.filter_by(name=item_name).first()
    if item.category.user_id != int(session['user_id']):
        return redirect_flash('You are not allowed to do this operation.', 'error')

    if item is None:
        return redirect_flash('Item not found.', 'error')

    if request.method == 'GET':
        return render_template('edit_item.html', item=item)

    elif request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if all([name, description]):  # is valid form
            item.name = name
            item.description = description

            db.session.add(item)
            db.session.commit()

            return redirect_flash('Successfully updated item name')

        else:
            return redirect_flash('Wrong fields editing item.',
                                  status='error')


@edit.route("/category/<category_name>", methods=['GET', 'POST'])
@logged
def edit_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    if category is None:
        return redirect_flash('Category not found.', 'error')
    if category.user_id != session['user_id']:
        return redirect_flash('You are not allowed to do this operation.', 'error')

    if request.method == 'GET':
        return render_template('edit_category.html', category=category)

    elif request.method == 'POST':
        name = request.form['name']

        if name:  # is valid form
            db.session.add(category)
            db.session.commit()

            return redirect_flash('Successfully updated item name')

        else:
            return redirect_flash('Wrong fields editing item.',
                                  status='error')
