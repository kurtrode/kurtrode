print ("This is a calculator.  Using z as an operator will end the program")

while True:
    x = input("+,-,*, or /   ")
    if x == "z":
        break
    if x in ("+", "-", "*", "/"):
        a = input("First number: ")
        b = input("Second number: ")
        if x == "+":
            print (int(a)+int(b))
        elif x == "-":
            print (int(a)-int(b))
        elif x == "*":
            print (int(a)*int(b))
        elif x == "/":
            if b == "0":
                print ("Cannot divide by zero!")
            else:
                print (int(a)/int(b))
    else:
        print ("Invalid operator!")
