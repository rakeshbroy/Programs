from colorama import init  #install colorama module by executing "pip install colorama" command without quotes.
from termcolor import colored  #install termcolor module by executing "pip install colorama" command without quotes.
init()
f = open('searchfile.txt')  #file should be in same directory where the search.py file resides.
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
