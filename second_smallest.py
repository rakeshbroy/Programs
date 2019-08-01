'''Program to find second smallest number in a list.'''
list = eval(input("Enter list:-"))
min = list[0] if list[0]<list[1] else list[1]
secondmin = list[0] if list[0]>list[1] else list[1]
for i in range(2,len(list)):
    if list[i] < min:
        secondmin = min
        min = list[i]
    elif list[i] > min:
        if list[i] < secondmin:
            secondmin = list[i]
print(secondmin)
