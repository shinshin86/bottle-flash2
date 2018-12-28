from bottle import Bottle, run, route, request, post, jinja2_template as template
from bottle_flash2 import FlashPlugin

# Flash Setup
app = Bottle()
COOKIE_SECRET = 'super_secret_string'
app.install(FlashPlugin(secret=COOKIE_SECRET))

@route('/')
def sample():
    return template('index.html', app = app)

@route('/done')
def done_get():
    return template('done.html', app = app)

@post('/done')
def done_post():
    app.flash("FLASH MESSAGE")
    app.flash(request.forms.get('message'))
        
    return template('done.html', app = app)

run(host='localhost', port=8080, debug=True)
