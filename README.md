# apitest
To run these files on your system ,following software are pre-requisites;
Python 2.7/3.0
Flask
PostgreSQL Server
Files and their description-
Stage1:
Get.py-To create a Get API
Post.py- To create a Post API
createdatabase.py-to create database using PostgreSQL Server and table.
New values and their locations are added to the database.
Database is queried in another api.
Stage2:
Two GET Apis are created and details of a particular position (latitude , longiude) are calculated using these apis using two methods.
Stage 3:
Data is parse from json file and stored in csv file. This csv file is then loaded in postgresql database table.
An API is made which checks the position of a co-ordinate and returns in which city that point lies. 

