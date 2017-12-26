from flask import Flask, request, render_template, session, flash


DATABASE = 'flaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'zdfsgvxcxfcv234edwed2332e23223erfcsdfdsew132ewdczfda'



app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
@app.route('/hello')
def hello() :
	return 'Hello, world'


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST' :
		if request.form['username'] != app.config['USERNAME'] :
			error = 'Invalid username'
		elif request.form['password'] != app.config['PASSWORD'] :
			error = 'Invalid password'
		else :
			session['logged_in'] =  True
			flash('You were logged in')
			return render_template('index.html')
	return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in')
	flash('You were logged out')
	return render_template('index.html')

if __name__ == '__main__':
	app.run()