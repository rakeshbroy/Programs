from colorama import init
from termcolor import colored
init()
f = open('searchfile.txt')
l = f.read().split(' ')
for word in l:
	print(word,end =' ')
print()
print()
s = input('Enter sub string: ')
print()
print()
print(colored("Words having '"+s+"' as substring",'green','on_red'))
for word in l:
	pos = word.find(s)
	if(pos != -1):
		print(colored(word,'white','on_red'),end=' ')
	else:
		print(word,end =' ')
