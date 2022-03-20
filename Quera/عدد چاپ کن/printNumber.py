n = input()
tmp = list(n)
for i in range(len(tmp)):
    if len(tmp) > 100:
        break
    key = int(tmp[i])
    print("{}: ".format(key),end="")
    for j in range(key):
        print(key,end="")
    print()