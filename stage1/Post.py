from flask import Flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request,redirect
from flask import current_app
#connection with database
Post=Flask(__name__)
Post.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:tree0112@localhost/testdb'
Post.debug=True
db = SQLAlchemy(Post)
# Creating our database model
class Pos(db.Model):
    __tablename__ = "geogaphic"
    key = db.Column(db.Integer(), primary_key=True)
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
def render_with_context(template, url='/post_location', **kw):
    with Get.test_request_context(url):
    return render_template(template, **kw)
# for Querying database
@Get.route('/')
def loc():
     # for seeing database
    locquery=Pos.query.all()
     # for specific query
    singlequery=Pos.query.filter_by(key="IN/110073").first()
    a=render_with_context('add_pin.html',singlequery=singlequery)
    return a
#for adding database
@Get.route('/post_location',methods=['POST'])
def post_location():
    # print(request.form)
    with Post.app_context():
        #getting the input 
        loca=Pos(request.form['pincode'],request.form['place_name'],request.form['admin_name1'],request.form['latitude'],request.form['longitude'],request.form['accuracy'])
        print("obj created")
        db.session.add(loca)
        db.session.commit()
        return redirect(url_for(' loc'))
        
if __name__=="__main__":
    Post.run()
