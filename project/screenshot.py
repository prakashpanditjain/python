import time

def countdown(t):
    while t:
        mins, sec = divmod(t, 60)
        timer = f'{min}:02d:{sec}:02d'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


    print('Fire in the hole!!')

t = input("Enter the countdown in second")

countdown(int(t))