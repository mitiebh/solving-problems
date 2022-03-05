"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
Max = 0
for i in range(100,1000):
    for j in range(i,1000):
        # if i*j palidrome print i*j
        p = i*j
        # check p is palidrome
        r = 0
        while(p>0):
            r = r * 10 + (p%10)
            p = p//10
        if(r == i*j):
            if(r > Max):
                Max = r
print(Max)
