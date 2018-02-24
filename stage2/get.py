from flask import Flask
from flask import jsonify
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect
from flask import current_app
import os
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))#connection with database
get=Flask(__name__)
get.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:tree0112@localhost/testdb'
get.debug=True
db = SQLAlchemy(get)
conn = psycopg2.connect(database = 'testdb', user = 'postgres', password = 'tree0112', host = 'localhost')
curs = conn.cursor()
# Creating our database model
class Pos(db.Model):
    __tablename__ = "dable"
    key = db.Column(db.String(9), primary_key=True)
    place_name = db.Column(db.String(200))
    admin_name1= db.Column(db.String(200))
    latitude=db.Column(db.Float())
    longitude=db.Column(db.Float())
    accuracy=db.Column(db.Integer())
 
    def __init__(self,key,place_name,admin_name1,latitude,longitude,accuracy):
        self.key=key;
        self.place_name=place_name;
        self.admin_name1=admin_name1;
        self.latitude=latitude;
        self.longitude=longitude;
        self.accuracy=accuracy;
    def _repr_(self):
        return '<Pos %r>' % self.key
lat=input("enter the latitude")
lon=input("enter the longitude")
lat=float(lat)
lon=float(lon)
def render_with_context(template, url='/', **kw):
    with get.test_request_context(url):
       return render_template(template, **kw)
@get.route('/')
def loc():
     # for seeing database
    locquery=Pos.query.all()
    return render_with_context('add_pin.html',singlequery=singlequery)
#get using postgres computation
@get.route('/get_using_postgres')
def get_using_postgres():
     curs.execute("select * from dable where (point(longitude,latitude) <@> point(%s,%s)) <= 500000;",[lon,lat])
     rows=curs.fetchall() 
     #return render_with_context('add_pin.html',rows=rows)
     return jsonify({"results" : rows})
# get using self computation
@get.route('/get_using_self')
def get_using_self():
    curs.execute("select * from ( select key, place_name,admin_name1,latitude, longitude, (3959 * acos (cos ( radians(%s) ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians(%s) ) + sin ( radians(%s) ) * sin( radians( latitude ) ) ) ) AS distance FROM dable order by distance) items where distance < 500000;",[lat,lon,lat])
    rowss = curs.fetchall()
    return jsonify({"results" : rowss})

if __name__=="__main__":
    get.run()
