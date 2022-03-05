"""
The sum of the squares of the first ten natural numbers is,
1² + 2² + 3² + ... + 10² = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + 3 + ... + 10)² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
s1 = 0
s2 = 0
for i in range(1,101):
    s1 += pow(i,2)
for i in range(1,101):
    s2 += i
s2 = pow(s2,2)
print(s2-s1)