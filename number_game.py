from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():

	if 'secret_num' not in session:
		session['hint'] = " "
		session['secret_num'] = random.randrange(0, 101)
	return render_template('index.html')

@app.route('/proccess', methods=['POST'])
def proccess():
	session['guess_num'] = int(request.form['num'])
	print session['guess_num']
	print session['secret_num']
	if session['guess_num'] > session['secret_num']:
		print "Too high"
		session['hint'] = "Too high"
		session['class'] = 'red'
	elif session['guess_num'] < session['secret_num']:
		print "Too low"
		session['hint'] = "Too low"
		session['class'] = 'blue'
	elif session['guess_num'] == session['secret_num']:
		print "Win"
		session['hint'] = "Win"
		session['class'] = 'pink'
	return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)
