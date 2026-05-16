from flask import Flask, render_template, request
import smtplib
import requests
import os


# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("google_app_pass")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template("contact.html", msg="successfully sent your Message!")
    else:
        return render_template("contact.html", msg="Contact Me")

@app.route("/form-entry", methods=['POST'])
def receive_data():
    #get theform data here
    ...
    
def send_email(name, email, phone, message):
        #send email using smtplib
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        print("Login successful")

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ppandit8888@gmail.com",
            msg=f"""subject: Hello You have got a new message from your Form\n\nName: {name} \nEmail:{email} \nPhone:{phone} \nMessage: {message}"""
        )
        print("Email sent successfully")
        connection.close()

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)

