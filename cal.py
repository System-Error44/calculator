import os,sys,time

#Colours
w = '\033[0m'
r = '\033[1;91m'
g = '\033[1;92m'
y = '\033[1;93m'
b = '\033[1;94m'
p = '\033[1;95m'
s = '\033[1;96m'

#Logo
logo = y+''' _____       _            _       _
/  __ \     | |          | |     | |
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   '''

l = g+"-------------------------------------------------"+w

#Home
def cal():
    os.system('clear')
    print (l)
    print (logo)
    print ()
    print (l)
    print ()
    print ("[1]  Calculator")
    print ("[2]  Exit")
    print ()
    i = int(input(y+">>> Enter Your Choice : "+s))
    if i==1:
        os.system('clear')
        print (l)
        print (logo)
        print ()
        print (l)
        print ()
        print ("[1]  Addition")
        print ("[2]  Substraction")
        print ("[3]  Devision")
        print ("[4]  Multiply")
        print ("[5]  Tables")
        print ()
        o = int(input(y+">>> Enter Your Choice : "+s))
        if o==1:
            print ()
            v1 = int(input(y+">>> Enter Your First Value : "+s))
            v2 = int(input(">>> Enter Your Second Value : "))
            print ()
            print (l)
            print ()
            print ("Your Answer is = ", (v1 + v2))
            print ()
            print (l)
            print ()
            input("Press Enter To Back")
            os.system('python cal.py')
        elif o==2:
            print ()
            v1 = int(input(">>> Enter Your First Value : "))
            v2 = int(input(">>> Enter Your Second Value : "))
            print ()
            print (l)
            print ()
            print ("Your Answer is = ", (v1 - v2))
            print ()
            print (l)
            print ()
            input("Press Enter To Back")
            os.system('python cal.py')
        elif o==3:
            print ()
            v1 = int(input(">>> Enter Your First Value : "))
            v2 = int(input(">>> Enter Your Second Value : "))
            print ()
            print (l)
            print ()
            print ("Your Answer is = ", (v1 / v2))
            print ()
            print (l)
            print ()
            input("Press Enter To Back")
            os.system('python cal.py')
        elif o==4:
            print ()
            v1 = int(input(">>> Enter Your First Value : "))
            v2 = int(input(">>> Enter Your Second Value : "))
            print ()
            print (l)
            print ()
            print ("Your Answer is = ", (v1 * v2))
            print ()
            print (l)
            print ()
            input("Press Enter To Back")
            os.system('python cal.py')
        elif o==5:
            print ()
            i = int(input("Type Your Table Number : "))
            print ()
            for t in range(1,11):
                q = f"{i} x {t} = {(i)*t}"
                print (g+q+w)
            print ()
            input("Press Enter To Back")
            os.system('python cal.py')
        else:
            print ()
            print ("Input Error")
            time.sleep(1.5)
            os.system('python cal.py')
    elif i==2:
        exit()
    else:
        print ()
        print ("Input Error")
        time.sleep(1.5)
        os.system('python cal.py')
cal()
