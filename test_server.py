from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def funkoshop():
	sitekey = '6LeoeSkTAAAAAA9rkZs5oS82l69OEYjKRZAiKdaF'
	return render_template('recaptcha.html', sitekey=sitekey)

@app.route('/')
def hottopic():
	sitekey = '6LdasBsTAAAAAJ2ZY_Z60WzgpRRgZVKXnqoad77Y'
	return render_template('recaptcha.html', sitekey=sitekey)

@app.route('/')
def home():
	return render_template('recaptcha.html')
	# return 'http://gecko.hottopic.com'

@app.route('/<store>')
def hello(store):
	if store == 'funkoshop':
		return funkoshop()
	elif store == 'hottopic':
		return hottopic()
	else:
		return 'No store'

app.run()