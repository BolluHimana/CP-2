"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position==0: 
        return 0
    elif position==1: 
        return 1
    else:
         return get_fib(position-1)+get_fib(position-2)