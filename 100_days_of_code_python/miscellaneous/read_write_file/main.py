import datetime

def decorator_function(func):
    def wrapper(*args, **kwargs):
        startTime = datetime.datetime.now()
        result = func(*args, **kwargs)
        endtime = datetime.datetime.now()
        print(f"time taken to execute the function: {func.__name__3}", (endtime - startTime).total_seconds(), " seconds")


# print(startTime)
@decorator_function
def main():
    for i in range(1,100000):
        if i == 2 or i ==3:
            print(i)
        else:
            for devider in range(2,i//2+1):
                if i % devider == 0:
                    break
                else:
                    print(i)
