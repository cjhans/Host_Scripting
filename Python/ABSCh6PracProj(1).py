#Data from the book
tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

#Initilaizing a new table to sort the data
newTable = {0:[], 1:[], 2:[], 3:[]}

#Create a for loop tio iterate through each list in tableData
for li in tableData:
    for i in range(len(li)):
        #Put each item of tableData into newTable by index
        newTable[i].append(li[i])

#Determine the longest list by number of total characters, default it to zero
longest = 0
#Iterate through newTable
for key, value in newTable.items():
    # determine the total characters in each list
    length = len(''.join(value))
    #If the length is the longest length so far, make that equal longest
    if length > longest:
        longest = length

#Loop through the newTable one last time, printing spaces infront of each list,
#equal to the difference between the length of the longest list and length of the current list
for key, value in newTable.items():
    print(' ' * (longest - len(''.join(value))) + ' '.join(value))