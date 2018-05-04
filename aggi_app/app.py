#!/usr/bin/env python3

import requests
from flask import Flask
from flask import jsonify
from flask_bootstrap import Bootstrap
from flask import render_template
#from helpers/parse import parser
import json
import os
#from helpers\mercury_parser import ParserAPI

app = Flask(__name__,  static_url_path='')
Bootstrap(app)

app._static_folder = 'static'
app.debug = True

# file names
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))  

stat_fold = os.path.join(SITE_ROOT, "static")
json_url = os.path.join(SITE_ROOT, "static", "options.json")





@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/news')
def get_data():
    return requests.get('https://www.huffingtonpost.com/entry/donald-trump-wiretapping-reaction_us_5aeb42b9e4b0c4f193201a43').content

@app.route('/bundle10.html')
def bundle10():
    return render_template('bundle10.html')
	
@app.route('/bundle20.html')
def bundle20():
    return render_template('bundle20.html')

@app.route('/bundle30.html')
def bundle30():
    return render_template('bundle30.html')
	
@app.route('/bundle45.html')
def bundle45():
    return render_template('bundle45.html')

@app.route('/article10.html')
def article10():
	#return requests.get('https://www.huffingtonpost.com/entry/trump-gop-tribute_us_5aeb3e81e4b041fd2d242c97').content
    return render_template('article10.html')
  
@app.route('/media10.html')
def media10():
    return render_template('media10.html')
	
	
@app.route('/article') 
def homepage():
    return ("Hello!!!")
  
    #return render_template('movies.html', movies=json.loads(r.text)['movies'])

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
	
	


if __name__ == "__main__":
    app.run()
   
