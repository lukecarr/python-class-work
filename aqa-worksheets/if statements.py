def task1():
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['num'] = int(input("Enter a whole number: "))
        except ValueError:
            print("Invalid whole number!")
            continue
        break
    if inputs['num'] % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
