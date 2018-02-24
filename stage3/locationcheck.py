import psycopg2
import json
from pprint import pprint
import numpy as np
from pprint import pprint
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
data = json.load(open('data.json'))
x=input("enter the value of latitude")
y=input("enter the value of longitude")
x=float(x)
y=float(y)
c=0
a=np.zeros(21)
i=0
while (i<21):
    polygon = Polygon(data["features"][i]["geometry"]["coordinates"][0])
    point = Point(y,x) 
    
    if (polygon.contains(point)==True):
        a[i]=1
        c=i
        pprint(data["features"][c]["properties"]["name"])
        break
    i=i+1
print("location not found")

