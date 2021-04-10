import os
from flask import Flask, render_template, request, url_for, Blueprint
from werkzeug.datastructures import FileStorage

# import our OCR function
from . import ci2

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

bp = Blueprint('ocr_app', __name__)

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
        # i just do it all in memory?
        extracted_text = ci2.ocr(b64_string)
        #extra white space is caused by \x0c
        return render_template('upload.html', msg='Successfully processed', extracted_text=extracted_text, results="results", img_src=b64_string_whole, code=301)
    elif request.method == 'GET':
        return render_template('upload.html', crop="yes")

# TODO:  Command line
# if __name__ == '__main__':
#     app.run()

