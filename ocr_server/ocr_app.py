import os
from flask import Flask, render_template, request, url_for, Blueprint
from werkzeug.datastructures import FileStorage
#b64 decode strip mime
#import base64

# import our OCR function
#from ocr_core import ocr_core
from . import ci2


# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

bp = Blueprint('ocr_app', __name__)

# def create_app(test_config=None):
#     #create and configure the app
#     app = Flask(__name__)
#     app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#     bp = Blueprint('app', __name__)
#     app.register_blueprint(app.bp)
#     return app

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the home page
#@app.route('/')
#def home_page():
    #return render_template('index.html')

# route and function to handle the upload page
@bp.route('/', methods=['GET', 'POST'])
@bp.route('/upload', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'b64_text_field' not in request.form:
            return render_template('upload.html', msg='No file selected')
        b64_string = str.encode(request.form['b64_text_field'].split(",")[1])
        b64_string_whole = request.form['b64_text_field']
        b64_name = request.form['b64_name']
        #file = FileStorage(content_type='image/png', filename='newImg242.png', name='image_placeholder', content_length=0, stream=b64_string)
        img_ready = "roiCrop_of_" + b64_name
        # with open("static/uploads/" + img_ready, "wb") as fh:
            # fh.write(base64.decodebytes(b64_string))

        # i just do it all in memory?
        #img_blob = base64.decodebytes(b64_string)
        extracted_text = ci2.ocr(b64_string)
        # extracted_text = ci2.ocr(img_ready)
        #extra white space is caused by \x0c
        return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text, results="results", img_src=b64_string_whole, code=301)

            #file = FileStorage(stream=fh, content_type='image/png', filename='newImg448.png',)
        #file = object
        #zachs debug
        #print(file.filename)
        ## if no file is selected
        #if file.filename == '':
        #    return render_template('upload.html', msg='No file selected')

        #if file and allowed_file(file.filename):
        #    file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], file.filename))

            ## call the OCR function on it
            #extracted_text = ocr_core(file)

            # call ci2 function on it
        #print("THIS IS THE FILE: " + file.filename)
        #extracted_text = ci2.ocr(file.filename)


        # extract the text and display it
        #print(url_for('static', filename='uploads/' + file.filename, code=301))

           # return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text, img_src=url_for('static', filename='uploads/' + file.filename), code=301)
    elif request.method == 'GET':
        return render_template('upload.html', crop="yes")

# TODO:  Command line
# if __name__ == '__main__':
#     app.run()

