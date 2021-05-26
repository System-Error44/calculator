import os
w = '\033[0m'
r = '\033[1;91m'
g = '\033[1;92m'
p = '\033[1;93m'
b = '\033[1;96m'
os.system('clear')
logo = ''' _____       _            _       _             
/  __ \     | |          | |     | |            
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   '''
print (g+logo+p)
print("")
print ("             Welcome To My Calculator")
print("")
print("[1]  Calculator")
print("[2]  Exit")
print ("")
print ("Enter Your Choice")
e = int(input())
print ("")
if e==1:
	v1 = int(input(r+"Enter Your First Value = "+b))
	print ("")
	v2 = int(input(r+"Enter Your Second Value = "+b))
	print ("")
elif e==2:
	exit()
else:
	print("input Error")
	os.system('clear')
	os.system('python2 cal.py')
print (p+"[1]  Addition")
print ("|")
print ("[2]  Substraction")
print ("|")
print ("[3]  Devision")
print ("|")
print ("[4]  Multiply"+r)
print ("")
i = raw_input("Enter Your Choice : "+g)
y = 'Your Answer is = '
z = '____________________________________________________'
if i=="1":
	print("")
	print (w+z)
	print("")
	print (y, (v1) + (v2))
	print ("")
	print (w+z)
	os.system('python2 cal.py')
elif i=="2":
	print("")
	print(w+z)
	print("")
	print (y, (v1) - (v2))
	print("")
	print (w+z)
	os.system('python2 cal.py')
elif i=="3":
	print("")
	print(w+z)
	print ("")
	print (y, (v1) / (v2))
	print ("")
	print(w+z)
	os.system('python2 cal.py')
elif i=="4":
	print("")
	print (w+z)
	print("")
	print (y, (v1) * (v2))
	print("")
	print(w+z)
	os.system('python2 cal.py')
else:
	print (r+"Wrong Input"+w)
	os.system('python2 cal.py')
