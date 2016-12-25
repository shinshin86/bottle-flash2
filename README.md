# Bottle-Flash2

####app.py

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


 {% set messages = app.get_flashed_messages() %}
 {% if messages %}
 <div id="flash_messages">
 <ul>
 {% for m in messages %}
 <li>{{ m[0] }}</li>
 {% endfor %}
 </ul>
 </div>
 {% endif %}






I will register as soon (Within the year == 2016).



# Motivation

I want to run "Bottle-Flash" in my environment.<br>

	Python 3.5.1

it seems this project that it has not been maintained.<br>
So I forked it.

# Licence

MIT