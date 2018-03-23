from flask import Flask
app = Flask(__name__)

@app.route('/guest/<name>')
def hello_guest(name):
  	return 'Hello %s!' % name
