from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautifu day in portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'Beautifu day in cool!'
        }
    ]
    return render_template('index.html', 
        title = 'Home',
        user = user,
        posts = posts
    )
    