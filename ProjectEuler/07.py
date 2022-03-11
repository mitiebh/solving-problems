# 10001th prime number
counter = 1
n = 3
while counter < 10001:
    c = 0
    for i in range(1,(n//2)+1):
        if n % i == 0:
            c += 1
    c += 1
    if c == 2:
        # n is prime
        counter += 1
        print(counter, n)
    n += 2