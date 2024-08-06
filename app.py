from flask import Flask,redirect,url_for,request,render_template;
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__);

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

if __name__=='__main__':
   app.run(debug=True)