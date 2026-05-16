from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST','GET'])
def submit():
    #get the form data
    name = request.form.get('username')
    password= request.form.get('password')
    return f"<h1>Hi {name}, You have successfully submitted the form!</h1>"



if __name__ == "__main__":
    app.run(debug=True)
