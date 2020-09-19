'''
Declaration of views and routes.
'''
from app import app


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return 'Home View'