from datetime import date

def leapYear(x):
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)

def task1():
    #Setup the Current Date
    current = {}
    current['date'] = date.today()
    current['year'] = current['date'].year
    current['month'] = current['date'].month
    current['day'] = current['date'].day
    del current['date']
    
    #Setup Maximum Month Days
    maximumDaysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
    maximumDaysInMonthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['year'] = int(input("Please enter the year you were born: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['year'] > current['year']:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['month'] = int(input("Please enter the month you were born: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['year'] == current['year'] and inputs['month'] > current['month']:
            print("Please enter a valid number!")
            continue
        if not (1 <= inputs['month'] <= 12):
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['day'] = int(input("Please enter the day you were born: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        if inputs['year'] == current['year'] and inputs['month'] == current['month'] and inputs['day'] > current['day']:
            print("Please enter a valid number!")
            continue
        if leapYear(inputs['year']):
            if inputs['day'] > maximumDaysInMonthLeap[inputs['month']-1]:
                print("Please enter a valid number!")
                continue
        else:
            if inputs['day'] > maximumDaysInMonth[inputs['month']-1]:
                print("Please enter a valid number!")
                continue
        break
    print("Your birthday has been validated to be " + str(inputs['day']).zfill(2) + "/" + str(inputs['month']).zfill(2) + "/" + str(inputs['year']))
        
def task2():
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['distance'] = int(input("Please enter the distance you ran in miles: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['time'] = int(input("Please enter the time taken in minutes: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        break
    while 1:
        try:
            inputs['decimals'] = int(input("Please enter the number of decimal places you would like: "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        break
    print("Your average pace was " + str(round(inputs['distance'] / inputs['time'], inputs['decimals'])) + " minutes per mile")
    
task2()