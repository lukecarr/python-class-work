def task1():
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['fahrenheit'] = float(input("Please enter the temperature to convert to Centigrade (in Fahrenheit): "))
        except ValueError:
            print("Please enter a valid temperature!")
            continue
        break
    print("Centigrade: " + str(round(5 * (inputs['fahrenheit'] - 32) / 9, 3)))
    
def task2():
    MoneyLeft = 50000
    print("Italian Holiday")
    print("Starting Balance: " + str(MoneyLeft))
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['food'] = float(input("Please enter the amount of euros spent on food: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['food'] < 0:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['trips'] = float(input("Please enter the amount of euros spent on trips: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['trips'] < 0:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['presents'] = float(input("Please enter the amount of euros spent on presents: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['presents'] < 0:
            print("Please enter a valid number!")
            continue
        break
    MoneyLeft -= inputs['food']
    MoneyLeft -= inputs['trips']
    MoneyLeft -= inputs['presents']
    print("Remaining Balance: " + str(MoneyLeft))
    
def task3():
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['people'] = int(input("Please enter the number of people travelling to the match: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['people'] < 0:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['capacity'] = int(input("Please enter the seating capacity of each coach (assuming all are the same): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['capacity'] < 0:
            print("Please enter a valid number!")
            continue
        break
    fullCoaches = inputs['people'] // inputs['capacity']
    finalCoach = inputs['people'] - (fullCoaches * inputs['capacity'])
    print("There will be " + str(fullCoaches) + " full coaches.")
    if finalCoach > 0:
        print("There will be an additional coach with only " + str(finalCoach) + " people aboard. (" + str(round(finalCoach / inputs['capacity'] * 100, 2)) + "% Full)")
        
def task4():
    #Get Inputs
    print("Enter start time for your journey (in 12 hour clock format).")
    inputs = {}
    inputs['start'] = {}
    inputs['taken'] = {}
    while 1:
        try:
            inputs['start']['hour'] = int(input("Hour: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if not (0 <= inputs['start']['hour'] <= 12):
            print("Please enter a valid hour!")
            continue
        break
    while 1:
        try:
            inputs['start']['minutes'] = int(input("Minutes: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if not (0 <= inputs['start']['minutes'] <= 59):
            print("Please enter a valid minute!")
            continue
        break
    print("\nEnter time taken (in 12 hour clock format).")
    while 1:
        try:
            inputs['taken']['hour'] = int(input("Hour: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if not (0 <= inputs['taken']['hour'] <= 11):
            print("Please enter a valid hour!")
            continue
        break
    while 1:
        try:
            inputs['taken']['minutes'] = int(input("Minutes: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if not (0 <= inputs['taken']['minutes'] <= 59):
            print("Please enter a valid minute!")
            continue
        break
    finishHour = (inputs['start']['hour'] + inputs['taken']['hour']) % 12
    if finishHour == 0:
        finishHour = 12
    finishMinutes = inputs['start']['minutes'] + inputs['taken']['minutes']
    if finishMinutes >= 60:
        finishMinutes -= 60
        finishHour += 1
    print("\nFinish time is: " + str(finishHour).zfill(2) + ":" + str(finishMinutes).zfill(2))