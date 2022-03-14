userin=int(input('Please input a number between 1 and 10:\n'))
if userin > 5:
    newuserin=userin*10
    start=1
    while start <= newuserin:
        print(start)
        start=start+1
elif userin < 5:
    newuserin=userin*5
    for i in range(newuserin):
        print(i+1)
elif userin == 5:
    newuserin=userin

print('The result is:'+ str(newuserin))