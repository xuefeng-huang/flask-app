from flask_init import app

@app.route('/')
@app.route('/index')
def index():
    return 'hello_world'