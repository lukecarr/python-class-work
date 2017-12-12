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

def task2():
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['age'] = int(input("Enter your age in years: "))
        except ValueError:
            print("Invalid number!")
            continue
        break
    while 1:
        inputs['passedTest'] = input("Have you passed your test? (Y/N) ").strip().upper()
        if inputs['passedTest'] != 'Y' and inputs['passedTest'] != 'N':
            print("Invalid response.")
            continue
        break
    if inputs['age'] >= 21 and inputs['passedTest'] == 'Y':
        print("You are allowed to drive the minibus.")
    else:
        print("You are not allowed to drive the minibus.")
        
def task3():
    print("Sorting Three Names:\n")
    #Get Inputs
    inputs = {}
    inputs['one'] = input("First name: ").strip().title()
    inputs['two'] = input("Second name: ").strip().title()
    inputs['three'] = input("Third name: ").strip().title()
    print(", ".join(sorted([inputs['one'], inputs['two'], inputs['three']])))