from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

user_comments = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", user_comments=user_comments)
    else: # post
        user_comments[request.form["uname"]] = request.form["contents"]
        return redirect(url_for('index'))

