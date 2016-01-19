# Fibonacci-exercise
Application question - Fibonacci

# Description of the exercise:
In the programming language of your choice, write a program 
generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

# How to run:
Call the function F() in Fib.py:
>> python -c 'import Fib; Fib.F(n)'

Example - To get F(8):
>> python -c 'import Fib; Fib.F(8)'

# How to test:
To test the program:
        >> python -m doctest -v Fib.py
        
5 tests included in the set:
1.
        >>> FibonacciProgram(0)

2.
        >>> FibonacciProgram(-3)
        'Invalid value, try again.'

3.
        >>> FibonacciProgram(5.2)
        'Invalid value, try again.'

4.      >>> FibonacciProgram(1)
        0

5.      >>> FibonacciProgram(10)
        0
        1
        1
        BuzzFizz
        Buzz BuzzFizz
        Fizz BuzzFizz
        8
        BuzzFizz
        Buzz
        34

