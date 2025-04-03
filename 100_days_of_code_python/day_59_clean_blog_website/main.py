from flask import Flask, render_template
import requests

#USE YOUR OWN npoint LINK! OTHERWISE IT WILL NOT WORK 👇
url = 'https://api.npoint.io/3903edb5f1acfbf6b124'
posts = requests.get(url).json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)