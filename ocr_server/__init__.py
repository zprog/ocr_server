import os
from flask import Flask

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__)
    # define a folder to store and later serve the images
    UPLOAD_FOLDER = 'static/uploads/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    #register blueprint
    from . import ocr_app
    app.register_blueprint(app.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
