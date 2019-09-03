# first_module.py

def addition():
    print("Add")
    print("x = {}".format(x))
    c = a + b 
    print("{} + {} = {}".format(a, b, c))
    return
    

if __name__ == "__main__":
    x = input("Input a command: ")
    print("You entered {}.".format(x))
    a = 1
    b = 2
    if x == 'add' or x == 'a':
        addition()
    else:
        print("{} is not an active command.".format(x))
        print("Enter a new command.")
    print("Done")



       