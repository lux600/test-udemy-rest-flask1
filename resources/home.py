from flask import render_template
from flask_restful import Resource
from flask import send_from_directory

class Home(Resource) :
# class Home() :
    def get(self):
        return {"message":'Hello World!'}
        # return render_template("../front_react/build/index.html")
