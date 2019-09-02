# first_module.py

def addition(x, y):
    print("Add")
    print("x = {}".format(x))
    c = x + y 
    print("{} + {} = {}".format(x, y, c))
    return
    
def subtraction():
    print("subtract")
    a = 1
    b = 2
    c = a - b 
    print("{} - {} = {}".format(a, b, c))
    return
    
def addsubtract(x, y, symbol):
    if symbol == "+":
        c = x + y 
    elif symbol == "-":
        c = x - y 
    else:
        c = "Unrecognized"
    return c 
    

if __name__ == "__main__":
    x = input("Input a command: ")
    print("You entered {}.".format(x))
    a = int(input("a = "))
    b = int(input("b = "))
    if x == 'add' or x == 'a':
        symbol = "+"
        answer = addsubtract(a, b, 5)
    elif x == "s":
        answer = addsubtract(a, b, "-")
    else:
        print("{} is not an active command.".format(x))
        print("Enter a new command.")
    print("c = {}".format(answer))  
    print("Done")



       