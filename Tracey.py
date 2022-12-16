import random
cards1 = {}
a=0
while True:
    z = input("Add cards to deck one? ")
    if z == "y" or z == "Y":
        y = input("Input value of card ")
        cards1.update({a:y})
        a=a+1
        x = input("Again? ")
        if x == "y" or x == "Y":
            continue
        else:
            #print(cards1)
            #break
            while True:
                b = input("Choose a card? ")
                if b == "y" or b == "Y":
                    c = random.choice(list(cards1.values()))
                    print (c)
                    for key, value in dict(cards1).items():
                        if value == c:
                            del cards1[key]
                    if len(cards1.keys()) == 0:
                        print ("Last card")
                        break
                    continue
                else:
                    break
        if len(cards1.keys()) == 0:
            continue
        else:
            break
    else:
        break
    #else:
    #    b = input("Choose a card? ")
    #    if b == "y" or b == "Y":
    #        c = random.choice(list(cards1.values()))
    #        print (c)
    #        continue
    #    else:
    #        break
