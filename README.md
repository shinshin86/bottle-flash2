# Bottle-Flash2----flash plugin for bottle.<br>(Bottle-Flash2 is a fork of [Bottle-Flash](https://pypi.python.org/pypi/bottle-flash/)).# Example

####app.py
~~~~
from bottle import Bottle, post, jinja2_template as template
from bottle_flash2 import FlashPlugin

# Flash Setup
app = Bottle()
COOKIE_SECRET = 'super_secret_string'
app.install(FlashPlugin(secret=COOKIE_SECRET))

@post('/flash_sample_done')
def flash_sample():
    app.flash("flash message is here")
    
    # flash mesage is stored in list
    # Therefore, it is possible to store a multiple messages.
    app.flash("flash message 1")
    app.flash("flash message 2")
        
    return template('index.html', app = app)
~~~~#### index.html
~~~~
 {% set messages = app.get_flashed_messages() %}
 {% if messages %}
 <div id="flash_messages">
 <ul>
 {% for m in messages %}
 <li>{{ m[0] }}</li>
 {% endfor %}
 </ul>
 </div>
 {% endif %}~~~~# Bottle version (Test environment)

	version 0.12.9 or above later.
	Latest Version -> '0.13-dev'
# Installation
You can install with this command.
	pip install bottle_flash2


# Motivation

I want to run "Bottle-Flash" in my environment.<br>

	Python 3.5.1	Bottle v0.12.9

it seems this project that it has not been maintained.<br>
So I forked it.

# Licence

MIT