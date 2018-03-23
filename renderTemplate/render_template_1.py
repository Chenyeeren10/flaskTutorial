from flask import Flask, render_template 
app = Flask(__name__) 
@app.route('/hello/<int:score>')
def hello_name(score):
	return render_template('render_template_1.html', marks=score)
