# coding: utf-8

from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
   return render_template('about.html')

@app.route('/post')
def post():
   return render_template('post.html')

@app.route('/housing')
def housing():
   return render_template('housing.html')

@app.route('/members')
def members():
   return render_template('members.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/archive')
def archive():
   return render_template('archive.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)