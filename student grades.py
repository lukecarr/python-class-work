input("Student Number: ")

tutorialMark = float(input("Tutorial Mark: "))
testMark = float(input("Test Mark: "))

if (tutorialMark + testMark) / 2 < 40:
    print("Grade: F")
    raise SystemExit

examinationMark = float(input("Examination Mark: "))
totalMark = tutorialMark + testMark + examinationMark * 2
totalPercentage = totalMark / 4

if totalPercentage >= 80:
    print("Grade: A")
elif totalPercentage >= 70:
    print("Grade: B")
elif totalPercentage >= 60:
    print("Grade: C")
elif totalPercentage >= 50:
    print("Grade: D")
else:
    print("Grade: E")
