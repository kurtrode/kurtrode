import random
import tkinter.messagebox
from tkinter import *
win=Tk()
win.title('Math Test')
win.geometry('800x600')
ent=Entry(win)
ent.pack()

blah = 3
def number():
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=random.randint(1,10)
        f=str(a)+" + "+str(b)+" + "+str(c)
        g=str(a)+" + "+str(b)+" - "+str(c)
        h=str(a)+" - "+str(b)+" + "+str(c)
        i=str(a)+" - "+str(b)+" - "+str(c)
        items = [1, 2, 3, 4]
        def rand():
            random.choice(items)
        if random.choice(items) == 1:
            j = a+b+c
            if j >= 0:
                txt=Text(win, height=3, width=50)
                txt.pack()
                txt.insert(INSERT,"str(a)+" + "+str(b)+" + "+str(c)")
                print (str(a)+" + "+str(b)+" + "+str(c))
                z = int(ent.get())
                if z == j:
                    msg='Correct'
                    break
                else:
                    msg='Sorry, No'
                    break
            else:
                continue
        elif random.choice(items) == 2:
            j = a+b-c
            if j >= 0:
                print (str(a)+" + "+str(b)+" - "+str(c))
                z = input()
                if z == j:
                    print ("Correct")
                    break
                else:
                    print ("Sorry, no")
                    break
            else:
                continue
        elif random.choice(items) == 3:
            j = a-b+c
            if j >= 0 and a-b > 0:
                print (str(a)+" - "+str(b)+" + "+str(c))
                z = input()
                if z == j:
                    print ("Correct")
                    break
                else:
                    print ("Sorry, no")
                    break
            else:
                continue
        elif random.choice(items) == 4:
            j = a-b-c
            if j >= 0:
                print (str(a)+" - "+str(b)+" - "+str(c))
                z = input()
                if z == j:
                    print ("Correct")
                    break
                else:
                    print ("Sorry, no")
                    break
            else:
                continue
number()
while True:
    x = "y"
    last = raw_input("Do you want to continue? y for yes, anything else for no: ")
    if last.lower() == x:
        number()
    else:
        exit()
