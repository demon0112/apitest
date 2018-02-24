#GET API
from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect


Get=Flask(__name__)
Get.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:tree0112@localhost/testdb'
Get.debug=True
db = SQLAlchemy(Get)
@Get.route('/')
   #statements
if __name__=="__main__":
    Get.run()
