def task1():
    #Get Inputs
    inputs = {}
    inputs['name'] = input("Please enter your name: ").strip().title()
    while 1:
        try:
            inputs['age'] = int(input("Please enter your age: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['age'] < 0:
            print("Please enter a valid age!")
            continue
        break
    while 1:
        try:
            inputs['year'] = int(input("Please enter the current year: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        break
    
    print("Nice to meet you " + str(inputs['name']))
    print("In the year " + str((100 - inputs['age']) + inputs['year']) + " you will be 100 years old.")

def task2():
    pi = 3.1415926
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['height'] = float(input("Please enter the height of cylinder: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['height'] < 0:
            print("Please enter a valid height!")
            continue
        break
    while 1:
        try:
            inputs['radius'] = float(input("Please enter the radius of cylinder: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['radius'] < 0:
            print("Please enter a valid radius!")
            continue
        break
    volume = pi * (inputs['radius'] ** 2) * inputs['height']
    surfaceArea = 2 * pi * inputs['radius'] * (inputs['radius'] + inputs['height'])

    print("The volume is " + str(volume))
    print("The total surface area is " + str(surfaceArea))
