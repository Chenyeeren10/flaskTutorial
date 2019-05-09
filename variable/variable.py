from flask import Flask
app = Flask(__name__)

@app.route('/guest/<name>')
def hello_guest(name):
  	return 'Hello %s!' % name


if __name__ == "__main__":
    app.run(port=5050)
