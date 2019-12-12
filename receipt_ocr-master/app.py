from flask import Flask, render_template, request

from werkzeug import secure_filename
import os
from os.path import join, dirname, realpath

import recognizer

UPLOAD_FOLDER = os.path.join(dirname(realpath(__file__)), 'receipt')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/uploader", methods = ["POST"])
def get_image():
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        recognizer.run_single(filename)

        
        return render_template("confirmation.html")
    
if __name__ == '__main__':
    app.run(debug=True)

    