from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/')
def student():
	return render_template('index.html')

@app.route('/result',methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        #insert your code here hint: what should you return and where should you return?
