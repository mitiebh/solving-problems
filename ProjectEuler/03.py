"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
x = 600851475143
i = 1
while(x > 1):
    i += 2
    # divide 2 factors
    while(x%2==0):
        x /= 2
    
    # divide other factors: 3,5,7,9,...,max
    while(x%i==0):
        x /= i
print(i)