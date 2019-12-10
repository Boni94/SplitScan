from flask import Flask, render_template, request

from werkzeug import secure_filename
import os
import recognizer

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/uploader", methods = ["POST"])
def get_image():
    picture = request.files['file']
    filename = secure_filename("receipt-"+picture.filename)
    picture.save(os.path.join('receipt', filename))
    recognizer.run_single(filename)
    return render_template("confirmation.html")
    
if __name__ == '__main__':
    app.run(debug=True)