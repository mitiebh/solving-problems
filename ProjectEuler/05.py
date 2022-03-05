"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
x = 20
while True:
    c = 0
    for i in range(11,21):
        if(x%i==0):
            c += 1
    if(c == 10):
        print(x)
        break
    x += 20