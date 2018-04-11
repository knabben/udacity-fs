from  sqlalchemy import desc
from models import db, Item, Category
from flask import Blueprint, render_template, session, request
from helpers import redirect_flash, logged


delete = Blueprint('delete', __name__, template_folder='../templates')


@delete.route("/item/<item_name>", methods=['GET', 'POST'])
@logged
def delete_item(item_name):
    if request.method == 'GET':
        return render_template('confirm_delete.html', item_name=item_name)

    elif request.method == 'POST':
        item = Item.query.filter_by(name=item_name).first()
        if item is None:
            return redirect_flash('Item not found.', 'error')
        if item.category.user_id != session['user_id']:
            return redirect_flash('You are not allowed to do this operation.', 'error')

        else:
            db.session.delete(item)
            db.session.commit()

            return redirect_flash('Item deleted.')


@delete.route("/category/<category_name>")
@logged
def delete_category(category_name):
    category = Category.query.filter_by(name=category_name).first()
    if category is None:
        return redirect_flash('Category not found.', 'error')

    else:
        db.session.delete(category)
        db.session.commit()

        return redirect_flash('Category deleted.')
