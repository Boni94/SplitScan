# flask is a Python micro web framework. It does not require particular tools or libraries.
# Flask is a Python class datatype. Flask  is the prototype used to create instances of web application.
# render_template to render a template
# request keeps track of the request-level data during a request
from flask import Flask, render_template, request

# Werkzeug is a WSGI utility library for Python. The WSGI is a simple calling convention for web servers to forward requests to web applications or frameworks.
# os module provides a way of using operating system dependent functionality.
# os.path.join() method to join one or more path components intelligently
# os.path.dirname() method to get the directory name from the specified path
from werkzeug import secure_filename
import os
from os.path import join, dirname, realpath

import recognizer

# os.path.join(dirname(realpath(__file__)) always returns the current working directory, 
# rather than the directory that __file__ is actually located in. 
# This breaks the ability to locate included files.
UPLOAD_FOLDER = os.path.join(dirname(realpath(__file__)), 'receipt')

#allowed extensions for the receipt
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Flask constructor takes the name of current module as argument
# config is subclass of a dictonary. 
# certain values are forwarded to the Flask object so you can read and write them
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# rsplit returns a list of the words in the string
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#  Flask has a built-in wrapper for generating routes in the form of @app.route ('/'). 
# @app is the name of the object containing our Flask app
#  That function is mapped to the home ‘/’ URL
@app.route("/")
def hello():
    return render_template("index.html")

# @app.route creates a route so you can see the application working
# it creates a connection between the URL ("/uploader", methods = ["POST"]) and a function that returns a response, in this case: render_template("confirmation.html")
@app.route("/uploader", methods = ["POST"])
def get_image():
    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        recognizer.run_single(filename)

        
        return render_template("confirmation.html")

# Python assigns the name "__main__" to the script when the script is executed. 
# If the script is imported from another script, the script keeps it given name (e.g. hello.py). 
# In our case we are executing the script. Therefore, __name__ will be equal to "__main__". 
# That means the if conditional statement is satisfied and the app.run() method will be executed. 
# This technique allows the programmer to have control over script’s behavior.    
# Notice also that we are setting the debug parameter to true. That will print out possible Python errors on the web page helping us trace the errors. 
# However, in a production environment, you would want to set it to False as to avoid any security issues.
if __name__ == '__main__':
    app.run(debug=True)

    