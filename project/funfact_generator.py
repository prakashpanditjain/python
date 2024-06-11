from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import requests
import json

def get_fun_fact():

    clear()

    put_html("<p align=""left""><h2><img src=""https://\
    media.geeksforgeeks.org/wp-content/uploads/ \
    20210720224119/MessagingHappyicon.png"" width=""7%""> \
                                                    Fun Fact Generator</h2></p> \
                                                                             ")
    # URL for the funfacts websites

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    response = requests.request("GET", url)

    data = json.loads(response.text)

    useless_fact = data["text"]
    # print(data)

    style(put_text(useless_fact), 'color:blue; font-size: 30px')
    put_buttons(
        [dict(label='Click me', value='outline-success',
              color='outline-success')], onclick=get_fun_fact)


if __name__ == '__main__':

    # Put a heading "Fun Fact Generator"
    put_html("<p align=""left""><h2><img src=""https://media.\
    geeksforgeeks.org/wp-content/uploads/20210720224119 \
    /MessagingHappyicon.png"" width=""7%""> \
    Fun Fact Generator</h2></p>")

    # hold the session for long time
    # Put a Click me button
    put_buttons(
        [dict(label='Click me', value='outline-success',
              color='outline-success')], onclick=get_fun_fact)
    hold()
# response = get_fun_fact()
# print(response)