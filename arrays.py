from random import randint

def task1():
    tvProgrammes = [input(str(x) + ". ") for x in range(1,6)]
    position = int(input("What position to find? "))
    ordinalSuffixes = ["st", "nd", "rd", "th", "th"]
    print("Programme at " + str(position) + str(ordinalSuffixes[position-1]) + " place is " + tvProgrammes[position-1])

def task2():
    diceRolls = [randint(1,6) for x in range(int(input("How many rolls: ")))]
    print("Sum: " + str(sum(diceRolls)))
    print("Average: " + str(sum(diceRolls) / len(diceRolls)))
    for rollValue in set(diceRolls):
        print(str(rollValue) + ": " + str(diceRolls.count(rollValue)))

def infinity():
    index = 0
    while True:
        yield index
        index += 1

def end():
    raise LukeException

def task3():
    sentences = list(end() if input("Add one more string? ('y' to continue or other to stop) ").strip().lower() != "y" else input("") for x in infinity())
    print("Number of strings with a length of at least 2 and matching first and last characters: " + str(len([x for x in sentences if len(x) >= 2 and x[0] == x[-1]])))

def task4():
    words = list(end() if input("Add one more word? ('y' to continue or other to stop) ").strip().lower() != "y" else input("") for x in infinity())
    n = int(input("Words must be greater than: "))
    [print(word) for word in words if len(word) > n]

def task5():
    word = input("Word to add: ")
    table = [char for char in word] + ([' '] * (36 - len(word)))
    table = [table[start:start+6] for start in range(0, 36, 6)]
