'''Program to find second largest number in a list.'''
list = eval(input("Enter list:-"))
max = list[0] if list[0]>list[1] else list[1]
secondmax = list[0] if list[0]<list[1] else list[1]
for i in range(2,len(list)):
    if list[i] > max:
        secondmax = max
        max = list[i]
    elif list[i] < max:
        if list[i] > secondmax:
            secondmax = list[i]
print(secondmax)
