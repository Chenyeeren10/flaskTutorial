from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

user_comments = {}

@app.route("/", methods=["GET", "POST"])  # hint: what is the methods we may use to differentiate two status?

def index():
    if request.method == "GET":  # hint: what if the user does not click the post button?
        return render_template("/", user_comments=user_comments)  # hint:what is the name for your main page?
    else: # post
        user_comments[request.form["uname"]] = request.form["contents"]
        return redirect(url_for("index"))   # hint: if we want to go back to index function, what should we do inside the redirect?
if_name_=="main"
app.run(port=5050) 

