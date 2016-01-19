from itertools import count, islice
import math as math
import sys

def IsPrime(q):
#  Function that returns TRUE if q is prime, otherwise it returns FALSE
        return q > 1 and all(q%i for i in islice(count(2), int(math.sqrt(q)-1)))

def F(m):
# Inputs: n - positive integer number
# The output follows the instructions of the Fibonacci Application Question.

### Testing ...
        """
        >>> F(0)
        >>> F(-3)
        'Invalid value, try again.'
        >>> F(5.2)
        'Invalid value, try again.'
        >>> F(1)
        0
        >>> F(10)
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
        """
### Checking m: it should be a positive integer
        try:
                n = int(str(m))
                if n < 0:
                        return("Invalid value, try again.")
        except ValueError:
                return("Invalid value, try again.")
        else:

### First numbers of Fibonacci
                series = [0,1]
                for ii in range(0,n):
                        if ii < 2:
                                print series[ii]
                        else:
                                series.append(series[ii-1] + series[ii-2])      # Next Fibonacci's number
                                if series[ii] == 3:                             # 3 is divisible by 3 and is also prime
                                        print 'Buzz', 'BuzzFizz'
                                elif series[ii] == 5:                           # 5 is divisible by 5 and is also prime
                                        print 'Fizz', 'BuzzFizz'
                                elif not series[ii]%3 and not series[ii]%5:     # divisible by 3 and 5
                                        print 'Buzz','Fizz'
                                elif not series[ii]%5:                          # divisible by 5
                                        print 'Fizz'
                                elif not series[ii]%3:                          # divisible by 3
                                        print 'Buzz'
                                elif IsPrime(series[ii]):                       # prime
                                        print 'BuzzFizz'
                                else:
                                        print series[ii]                        # Not divisible by 3, 5 and not prime
                return
