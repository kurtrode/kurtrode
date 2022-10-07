import random
while True:
    a=random.randint(1,10)
    b=random.randint(1,10)
    if a>b:
        print("What is " + str(a) + "-" + str(b) + "?")
    else:
        print("What is " + str(a) + "+" + str(b) + "?")
    input_a = input()
    if a>b and input_a == a-b:
        print ("Correct")
    elif a<b and input_a == a+b:
        print ("Correct")
    else:
        print ("No")
    
