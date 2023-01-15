from flask import Flask, jsonify,  render_template, url_for, request
import json
import pyexcel
#import flask_ext_autodoc
from flask_restful import Api, Resource
#from flask_selfdoc import Autodoc
#from flask_autodoc import Autodoc
# in order to use the app, you must create an instance of the app 
app = Flask(__name__)
# synatax to create flask instance 
api =   Api(app)
#auto = Autodoc(app)
#syntax for decorators 
# create a method to display on the homepage/default page 

# @app.route("/") # define the page where the informatuon is being displayed (route of the page)

# def index_page():
#     return "<h1>Welcome to Flask MVC project</h1>"

# the index_page method will be called at the endpoint (where it is being displayed)

# syntax to run app 

@app.route("/")

def welcome_user():
    return render_template("base.html")

@app.route("/hello")

def hello():
    return render_template("hello.html")
@app.route("/hello1")

def hello1():
    return render_template("hello1.html")
@app.route("/logging/")

def welcome_use():
    return render_template("index.html")
# importing a html file from using render_template - include the name of the file in the brackets 

@app.route("/word/")

def word():
    return render_template("word.html")
# importing a html file from using render_template - include the name of the file in the brackets 

@app.route("/excel/")

def excel():
    return render_template("excel.html")
# importing a html file from using render_template - include the name of the file in the brackets 


@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    return render_template("paraform.html")
    


@app.route('/json-example', methods=['POST'])
def json_example():
    json12=jsonify(request.get_json(force=True));
    y = json.loads(json12.data)
    print(y.get('elem_a1'))
    print(y.get('elem_c13'))
    pyexcel.excel(y)
    return json12


# @app.route('/returnjson1', methods = ['GET'])
# def ReturnJSON():
    # if(request.method == 'GET'):
        # data = {
            # "Modules" : 15,
            # "Subject" : "Data Structures and Algorithms",
        # }
  
        # return jsonify(data)

# # This route generates documentation in list 
# # of rules
# @app.route('/documentation')
# def documentation():
    # return str(auto.generate())


if __name__ == "__main__":
    app.run(debug=True)