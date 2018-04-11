from flask import Flask 
from helpers import create_db
from models import db

from blueprints.listing import listing
from blueprints.detail import detail
from blueprints.edit import edit
from blueprints.delete import delete
from blueprints.add import add
from blueprints.login import login


app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(listing)
app.register_blueprint(detail, url_prefix='/catalog/detail')
app.register_blueprint(edit, url_prefix='/catalog/edit')
app.register_blueprint(delete, url_prefix='/catalog/delete')
app.register_blueprint(add, url_prefix='/catalog/add')
app.register_blueprint(login, url_prefix='/login')
db.init_app(app)


if __name__ == "__main__":
    # Initialize database
    create_db(app)
    app.run(debug=True)
