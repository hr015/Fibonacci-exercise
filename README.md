# Fibonacci-exercise
Application question - Fibonacci

# Description of the exercise:
In the programming language of your choice, write a program 
generating the first n Fibonacci numbers F(n), printing ...
- ... "Buzz" when F(n) is divisible by 3.
- ... "Fizz" when F(n) is divisible by 5.
- ... "BuzzFizz" when F(n) is prime.
- ... the value F(n) otherwise.

Programming language used: Python

# How to run:
From bash terminal, call the function F() in Fib.py:

        python -c 'import Fib; Fib.F(n)'

Example - To get F(8):

        python -c 'import Fib; Fib.F(8)'

# How to test:
To test the program doctest is used. From bash terminal:

        python -m doctest -v Fib.py
        
Five tests are included in the set:

1.      > F(0)

2.      > F(-3)
        'Invalid value, try again.'

3.      > F(5.2)
        'Invalid value, try again.'

4.      > F(1)
        0

5.      > F(10)
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

