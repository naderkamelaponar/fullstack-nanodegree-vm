from flask import Flask , render_template,request,redirect,url_for,jsonify
from sqlalchemy import create_engine
from database_setup import Base,Restaurant,MenuItem
engine= create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind=engine

app= Flask(__name__)
@app.route('/')
def Home():
    return 'welcome'
@app.route('/ok')
def Ok() :
    return 'Allah'
@app.route('/yes')
def Yes() :
    return 'yes'
if __name__ == '__main__':
    app.debug= True
    app.run(host='0.0.0.0',port=3000)
