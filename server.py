from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods = ["POST"])
def process():
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		return redirect('/') # just pass a string to the flash function
  	else:
  		# flash("Success! Your name is {}".format(request.form['name']))
  		session['name'] = request.form['name']
	
	if len(request.form['coms']) < 1:
		flash("Comments cannot be empty!")
		return redirect('/') # just pass a string to the flash function
  	elif len(request.form['coms']) > 120:
  		flash('Shorten it')
  		return redirect('/')
  	else:
  		# flash("Success! Your name is {}".format(request.form['name']))
  		session['coms'] = request.form['coms']

  	session['location'] = request.form['location']
	session['language'] = request.form['language']
	return render_template("results.html")

app.run(debug=True)