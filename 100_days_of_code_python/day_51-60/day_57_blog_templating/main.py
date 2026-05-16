import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_blogs = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=all_blogs)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog in all_blogs:
        print(blog["id"])
        if blog["id"] == index:
            requested_post = blog

    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
