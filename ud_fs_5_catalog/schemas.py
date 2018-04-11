from models import Category, Item, db
from marshmallow import fields
from flask_marshmallow.sqla import ModelSchema


class CategorySchema(ModelSchema):
    class Meta:
        model = Category
        sqla_session = db.session
        exclude = ('category',)

    items = fields.Nested(
        'ItemSchema',
        many=True,
        dump_only=True,
    )

class ItemSchema(ModelSchema):
    class Meta:
        model = Item


many_category_schema = CategorySchema(many=True)
