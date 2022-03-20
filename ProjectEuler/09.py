"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
            
            a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# ::::::::: Euclid's formula ::::::::::::
# for m>n>0 and k for coeficient we have:
# a = k(m² - n²)
# b = k(2×m×n)
# c = k(m² + n²)
for n in range (1,10):
    for m in range (n+1,11):
        a = pow(m,2)-pow(n,2)
        b = 2*m*n
        c = pow(m,2)+pow(n,2)
        for k in range (1,101):
            #print (k*a,k*b,k*c)
            if ((k*a)+(k*b)+(k*c) == 1000):
                #print ("m =",m,"n =",n)
                #print (a,b,c,",k =",k)
                #print (k*a,k*b,k*c)
                ans = (k*a)*(k*b)*(k*c)
                print ("ans =",ans)
                exit()
            
        #print (n,m)