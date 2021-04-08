import os
from  used_inventory.api_secrets import SUPER_SECRET_DB_KEY
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #register blueprint
    from . import app
    app.register_blueprint(app.bp)
    return app
