import random
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
                print (str(a)+" + "+str(b)+" + "+str(c))
                z = input()
                while True:
                    try:
                        z = int(z)
                        break
                    except ValueError:
                        print ("What?")
                        again()
                if int(z) == j:
                    print ("Correct")
                    break
                else:
                    print ("Sorry, no ")
                    break
            else:
                continue
        elif random.choice(items) == 2:
            j = a+b-c
            if j >= 0:
                print (str(a)+" + "+str(b)+" - "+str(c))
                z = input()
                while True:
                    try:
                        z = int(z)
                        break
                    except ValueError:
                        print ("What?")
                        again()
                if int(z) == j:
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
                while True:
                    try:
                        z = int(z)
                        break
                    except ValueError:
                        print ("What?")
                        again()
                if int(z) == j:
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
                while True:
                    try:
                        z = int(z)
                        break
                    except ValueError:
                        print ("What?")
                        break
                if int(z) == j:
                    print ("Correct")
                    again()
                else:
                    print ("Sorry, no")
                    break
            else:
                continue
def again():
    while True:
        x = "y"
        last = input("Do you want to continue? y for yes, anything else for no: ")
        if last.lower() == x:
            number()
        else:
            exit()
number()
again()
