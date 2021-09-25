from flask import Flask,request
from flask import render_template
from . import project

def add():
    return 2+5

def create_app():

    app = Flask("project_app")
    
    @app.route("/",methods = ['POST' , 'GET'])
    def index():
        if request.method == 'GET':
            return render_template("index.html",a = add())
        elif request.method == 'POST':
            weburl = request.form.get("webpageurl")
            
            hyperlinks = project.get_links(weburl)
            wronglinks = project.test_links(hyperlinks)
            return render_template("listurls.html",links=wronglinks)
    return app

