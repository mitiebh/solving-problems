s = input()
vowels = "oiaue"
c = 0
for i in range(len(s)):
    if s[i] in vowels:
        c+=1
print(c)
