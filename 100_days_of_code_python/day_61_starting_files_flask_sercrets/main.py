from flask import Flask, render_template, request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)

class myForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(),Email()], render_kw={"placeholder": "Enter your email"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)],  render_kw={"type": "password"})
    submit = SubmitField(label='Log In')

app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = myForm()
    admin_email= 'admin@email.com'
    admin_pass = "12345678"
    print(login_form.email.data,login_form.password.data,login_form.validate_on_submit())
    if login_form.validate_on_submit():
        print("inside the if condition")
        if login_form.email.data == admin_email and login_form.password.data == admin_pass:
            print("inside success.html")
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
