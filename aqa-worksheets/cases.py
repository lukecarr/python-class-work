def task1():
    print("Exam Grades\n")
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['mark'] = int(input("Mark out of 100: "))
        except ValueError:
            print("Invalid number!")
            continue
        if not (0 <= inputs['mark'] <= 100):
            print("Invalid mark!")
            continue
        break
    if inputs['mark'] < 40:
        grade = 'U'
    elif 40 <= inputs['mark'] <= 49:
        grade = 'E'
    elif 50 <= inputs['mark'] <= 59:
        grade = 'D'
    elif 60 <= inputs['mark'] <= 69:
        grade = 'C'
    elif 70 <= inputs['mark'] <= 79:
        grade = 'B'
    else:
        grade = 'A'
    print("\nGrade " + grade)

def task2():
    print("Discount Orders\n")
    #Get Inputs
    inputs = {}
    while 1:
        try:
            inputs['value'] = int(input("Value of Order: "))
        except ValueError:
            print("Invalid number!")
            continue
        if not (0 <= inputs['value'] <= 25000):
            print("Invalid order value!")
            continue
        break
    if inputs['value'] < 1000:
        multiplier = 1
    elif 1000 <= inputs['value'] < 2500:
        multiplier = 0.95
    elif 2500 <= inputs['value'] < 5000:
        multiplier = 0.9
    elif 5000 <= inputs['value'] < 10000:
        multiplier = 0.85
    else:
        multiplier = 0.8
    print("\nThe discounted price is " + str(inputs['value'] * multiplier))
