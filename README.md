python-fizzbuzzes
===

This Python package is designed to return FizzBuzz from a variety of methods!

Mostly this is just a bit of fun inspired by [a post at reddit](http://www.reddit.com/r/python/comments/22m7ew/) about [this blog post](http://skien.cc/blog/2014/04/09/unpythonic-python/).
The plan is to add silly methods to this now and again.


Quick examples:

```
from fizzbuzzes import FizzBuzz

# Create FizzBuzz object, optionally specifying type.
fizzbuzz = FizzBuzz(
    class_type=FizzBuzz.TYPE_MAP_SLICE
)

# FizzBuzz generator into a list
fizzbuzz_output = list(fizzbuzz.generate(limit=100))

# Get a string of FizzBuzz, optionally specifying separator
fizzbuzz_string = fizzbuzz.string(
    limit=100,
    separator="\n"
)

# Print out FizzBuzz, optionally specifying separator
fizzbuzz.print_output(
    limit=100,
    separator="\n"
)

```
