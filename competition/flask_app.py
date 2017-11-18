# [START app]
import logging
import subprocess
import time
from flask import Flask, render_template
import send_email_lemay
#import send_email_cave
import datetime

# [START imports]
from flask import Flask, render_template, request
# [END imports]

# [START create_app]
app = Flask(__name__)
# [END create_app]


# [START form]
@app.route('/form')
def form():
    return render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']

    # [END submitted]
    # [START render_template]
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'competition report',
      'time': timeString
      }
   if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            pass
            #print 'I got clicked!'
        elif request.form['submit'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
   return render_template('main.html', **templateData)

@app.route('/lemay', methods=['POST'])
def view_do_something():

    if request.method == 'POST':
        send_email_lemay.main("djgraff1@cougars.ccis.edu")
        #your database process here
        #subprocess.call(['python2.7', 'send_email_lemay.py'])
        #time.sleep(400)

        return "OK"

    else:
        return "NO OK"




@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]