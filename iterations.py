from random import randint
from time import clock
import statistics

class Timers:
  def task1():
    counter = int(input("Count to what? "))
    start = clock()
    for x in range(counter):
      pass
    print(str(clock() - start) + " seconds")

class Exercises:
  def task1():
    number = int(input("Times Table: "))
    print("\n".join([str(x) + " x " + str(number) + " = " + str(number * x) for x in range(1,13)]))
    
  def task2():
    sides = int(input("How many sides? "))
    rolls = [randint(1,sides) for x in range(1, 31)]
    print("\n".join(["Roll #" + str(x) + ": " + str(rolls[x]) for x in range(30)]))
    print("Average: " + str(sum(rolls) / 30))

  def task3():
    times = int(input("How many rolls? "))
    start = time()
    for x in range(times):
        randint(1, 6)
    print("Time taken: " + str(time() - start) + " seconds")

  def task4():
    total = 0
    rolls = 0
    start = time()
    while total < 6000:
      total += randint(1, 6)
      rolls += 1
    print("Time taken: " + str(time() - start) + " seconds")
    print("Expected # of Rolls is 1715.")
    print("Rolls taken: " + str(rolls))
    print("Average roll: " + str(total / rolls))

  def extension():
    iterAmount = int(input("How many simulations? "))
    rollAmount = int(input("How many rolls per simulation? "))
    simulations = []
    for h in range(iterAmount):
      rolls = []
      for i in range(rollAmount):
        rolls.append((randint(1,6), randint(1,6)))
      combinedRolls = [x+y for (x, y) in rolls]
      simulations.append((rolls, combinedRolls))
    for index, (rolls, combinedRolls) in enumerate(simulations):
      print("\nSimulation #%d" % index)
      print("Mean %s" % statistics.mean(combinedRolls))
      try:
        print("Mode %s" % statistics.mode(combinedRolls))
      except statistics.StatisticsError:
        print("Mode is undefined")
      print("Median %s" % statistics.median(combinedRolls))
      #with open("distrib #%d.csv" % index, "w") as csvFile:
        #for roll in rolls:
          #csvFile.writelines("%d\n" % (roll[0] + roll[1]))
