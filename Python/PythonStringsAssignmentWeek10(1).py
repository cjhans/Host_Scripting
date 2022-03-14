#in var1 appends the specified letty by inputting it in front of every letter but the last
var1='e'.join('nvr')
#in var2 the [::-1] reads the string backwards and returns 'gonna. the '::" tells it to go to the beginning of the string'
var2='annog'[::-1]
#in var3 the [-4] starts from the end of the string and works in 4 spaces. The the ':' tells it to return to the end of the srting
var3='forgive'[-4:]
#in var4 the [1] chooses the string in the 1 position of the array, being 'you' since it starts at 0
var4=('me', 'you')[1]
#in var5 the split function cuts off the string starting and including 'o'
var5='soup'.split('o')[1]

#never gonna give you up
print (var1,var2,var3,var4,var5)