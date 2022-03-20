saatInput = input().split(' ') # ['h','mm']
saatAns = ['',''] # ['hh','mm']

# hh section
if int(saatInput[0]) >= 6:
    ans = 12 - int(saatInput[0])
    saatAns[0] = str(ans)
if int(saatInput[0]) < 6:
    ans = - int(saatInput[0]) + 12
    saatAns[0] = str(ans)

if saatAns[0] == '12':
    saatAns[0] = '00'
if len(saatAns[0]) == 1:
    saatAns[0] = '0' + saatAns[0]

# mm section
if int(saatInput[1]) >= 30:
    ans = 60 - int(saatInput[1])
    saatAns[1] = str(ans)
if int(saatInput[1]) < 30:
    ans = - int(saatInput[1]) + 60
    saatAns[1] = str(ans)

if saatAns[1] == '60':
    saatAns[1] = '00'
if len(saatAns[1]) == 1:
    saatAns[1] = '0' + saatAns[1]

print(saatAns[0]+":"+saatAns[1])
