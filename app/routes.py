from flask import render_template
from app import app  

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bob'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username' : 'Susan'},
            'body' : 'Cake is nice'
        }
    ]
    return render_template('index.html', title = 'Home', user=user, posts=posts)