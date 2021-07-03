from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Javier'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Welcome to my world'
    },
    {
      'author': {'username': 'Susan'},
      'body': 'There are better things to do'
    }
  ]
  
  return render_template('index.html', title='Home', user=user, posts=posts)