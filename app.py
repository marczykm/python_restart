#!/usr/bin/python
import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

base_path = '/home/osmc/python_restart/'

password = 'osmc'

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/js/<path:path>")
def send_js(path):
	return send_from_directory(base_path + 'js', path)

@app.route("/css/<path:path>")
def send_css(path):
	return send_from_directory(base_path + 'css', path)

@app.route("/shutdown")
def shutdown():
	os.system('echo %s|sudo -S %s' % (password, 'shutdown now') )
	return "shutdown"

@app.route("/restart")
def restart():
	os.system('echo %s|sudo -S %s' % (password, 'reboot') )
	return "restart"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
