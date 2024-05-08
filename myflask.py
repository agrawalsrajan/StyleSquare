from flask import Flask, render_template
from flask import *
from functools import wraps
import sqlite3

app = Flask(__name__, template_folder='templatefiles', static_folder='staticfiles')

@app.route('/')
def home():
    return render_template('mini.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/tryon', methods=['POST'])
def tryon():
   print("Hello")
   return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)