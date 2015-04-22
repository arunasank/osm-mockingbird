from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/aruna')
@app.route('/appa')
def index():
	user = {'name':'aruna'}
	posts = [
		{
			'author':{'name':'Meenu'},
			'body': 'Eat on time!'
		},
		{
			'author':{'name':'Raajam'},
			'body':'Rajam sofa, meenu chair!'
		}
	]

	return render_template('index.html',
			        title='First Page',
				user=user,
				posts=posts)
