"""
Here’s another useful example for a generator: Generating an Infinite Fibonacci Sequence. This approach is
particularly effective when you need to generate an unbounded sequence of values without pre-defining its end,
which is impossible with standard lists or iterators.

Use Case: Generating the Fibonacci Sequence

Imagine you need a function that generates Fibonacci numbers on demand. Instead of calculating or storing all values
upfront (which is infeasible for an infinite sequence), you can use a generator to yield the next Fibonacci number
each time it’s requested.

Solution with a Generator

Using a generator, you can create a function that yields Fibonacci numbers endlessly until you decide to stop.
"""
import sys

# sys.set_int_max_str_digits(10000000)

def fibonacci(x):
    a, b = 0, 1
    counter = 1
    while counter < x:
        yield a
        a, b = b, a + b
        counter += 1

fib = fibonacci(1000000000000)
for number in fib:
    print(number)