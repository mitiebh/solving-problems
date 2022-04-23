n = int(input())
if n%2==1:
    c = 0
    for i in range(1,n//2+1):
        if n%i==0:
            c += 1
    c += 1
    if c==2:
        print("zoj")
    else:
        print("fard")
else:
    print("fard")
