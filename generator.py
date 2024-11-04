def counter(max):
    current = 0
    while current < max:
        current += 1
        yield current
for count in counter(5):
    print(count)
