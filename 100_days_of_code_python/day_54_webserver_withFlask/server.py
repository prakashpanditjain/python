from flask import Flask
import random
from functools import wraps

app = Flask(__name__)

def generate_random_number():
    num = random.randint(1,9)
    return num

random_num = generate_random_number()
print(random_num)

def make_center(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        return f"<center>{function(*args,**kwargs)}</center>"
    return wrapper


@app.route('/')
@make_center
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/dQ4Bgez5wkCcsX9dOP/giphy.gif?cid=790b7611zirmbfr9shguomqlhrhzg7qau7y5tdbhx0r8jkyo&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

@app.route('/<int:guess>')
@make_center
def num_route(guess):
    if guess < random_num:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/0n9qqn9Sv8PHwMutrq/giphy.gif?cid=790b7611ss68nb8jxz86iutx29yitqt7ir7uopnl6x1d87d5&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif guess > random_num:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/bobVgSksnUOyOzvDGU/giphy.gif?cid=790b7611zrqicabhqngqxi6keunerhqi1lnftf21d8rk7fnf&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnBtd2EzYXdsdDNjb2NiNXVpY2xlbTN0MXFlbW4xZWs4aXl6OWFlaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l1J9wXoC8W4JFmREY/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)