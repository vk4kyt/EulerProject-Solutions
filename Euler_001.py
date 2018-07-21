# Euler Problem 001
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

# import numpy

TopNumber = 1000
SumTotal = 0

for x in range(0, TopNumber):
    if ((x % 3 == 0) or (x % 5 == 0)):
        SumTotal = SumTotal + x
print (SumTotal)
