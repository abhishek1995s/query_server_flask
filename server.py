from flask import Flask,render_template,request,redirect,url_for,flash,jsonify
import requests

from rss_generator import passer
import json

app=Flask(__name__)
@app.route('/')
def initial():
    
        return render_template('index.html',result=' ')
    #else:
        #return render_template('newmenu.html',restaurant_id=restaurant_id)  
@app.route('/query', methods=['GET', 'POST'])
def query_processor():
        query=request.form['query']
        s_engine =request.form['s_engine'] 
        result= passer(query,s_engine)
        #print(result)
        tr=result.decode().split('/n')
        for m in tr:
            print(m)
    
        return render_template('index.html',result=tr)

@app.route('/query/<string:s_engine>/<string:query>/', methods=['GET', 'POST'])
def querye(s_engine,query):
    result= passer(query,s_engine,1)

    return json.dumps(result)


if __name__=='__main__':
    app.secret_key='super_secret_key'
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
