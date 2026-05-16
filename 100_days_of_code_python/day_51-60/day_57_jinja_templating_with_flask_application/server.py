import requests
from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

def centralize(fun):
    def wrapper(*args, **kwargs):  # Ensure arguments are passed properly
        return f"<br><center>{fun(*args, **kwargs)}</center><br>"
    return wrapper  # Do NOT call wrapper()

@app.route('/')
def home():
    year_ = datetime.today().date().year
    return render_template("index.html", year=year_)

@app.route('/guess/<name>')
@centralize
def guess(name):
    header = {
        "name" : "prakash"
    }

    response = requests.get("https://api.agify.io/", params=header)
    age_text = response.json()['age']

    gender_reponse = requests.get(f"https://api.genderize.io/?name={name}")
    gender_text = gender_reponse.json()['gender']

    return render_template("guess.html", name = name,age=age_text, gender = gender_text)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response= requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts= all_posts)

if __name__ == '__main__':
    app.run(debug=True)