import random
import time
import mmap
import heapq

def task1():
    with open('series5.txt', 'w') as file:
        file.writelines([x.strip() + "\n" for x in input("Enter 5 TV Programmes (separated by commas): ").split(",")])

def task2():
    with open('sequential5.txt', 'w') as file:
        file.writelines(sorted([x.strip() + "\n" for x in input("Enter 5 TV Programmes (separated by commas): ").split(",")]))

def task3():
    lines = None
    with open('series5.txt') as file:
        lines = file.readlines()
    del lines[3]
    with open('series5.txt', 'w') as file:
        file.writelines(lines)

def task4():
    lines = None
    with open('sequential5.txt') as file:
        lines = file.readlines()
    del lines[3]
    with open('sequential5.txt', 'w') as file:
        file.writelines(lines)

def task5():
    task1()
    lines = None
    with open('series5.txt') as file:
        lines = file.readlines()
    lines = sorted(lines)
    del lines[3]
    with open('series5.txt', 'w') as file:
        file.writelines(lines)

def task6setup():
    with open('random1million.txt', 'w') as file:
        for x in range(1000000):
            file.write(str(random.randint(1,100)) + "\n")

def task6():
    print("Starting reading line by line...")
    start = time.time()
    numbers = []
    with open('random1million.txt') as file:
        for line in file.readlines():
            numbers.append(int(line))
    duration = time.time() - start
    print("Time taken: " + str(duration) + " seconds")
    print("Starting reading char by char...")
    start = time.time()
    numbers = []
    with open('random1million.txt') as file:
        numbers = [int(x) for x in file.read().strip().split("\n")]
    duration = time.time() - start
    print("Time taken: " + str(duration) + " seconds")
    print("Starting with mmap...")
    start = time.time()
    numbers = []
    with open('random1million.txt') as file:
        m = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        while True:
            line = m.readline()
            if line == '' or line == b'': break
            numbers.append(int(line))
    duration = time.time() - start
    print("Time taken: " + str(duration) + " seconds")
    print("Starting binary reading line by line...")
    start = time.time()
    numbers = []
    with open('random1million.txt', 'rb') as file:
        for line in file.readlines():
            numbers.append(line)
    duration = time.time() - start
    print("Time taken: " + str(duration) + " seconds")
    print("Starting binary reading char by char...")
    start = time.time()
    numbers = []
    with open('random1million.txt', 'rb') as file:
        numbers = [int(x) for x in file.read().split()]
    duration = time.time() - start
    print("Time taken: " + str(duration) + " seconds")

def task7():
    with open(input("File to count lines: ")) as file:
        print("Number of Lines: " + str(len(file.readlines())))

def task8():
    words = []
    with open('words.txt') as file:
        words = [[char for char in x.strip()][0] for x in file.read().split("\n") if x.strip() != '']
    frequencies = {char:words.count(char) for char in set(words)}
    print(frequencies)

def task9():
    with open('words.txt') as file:
        print("10 Biggest Words:")
        [print(x) for x in heapq.nlargest(10, [x.strip() for x in file.read().split("\n") if x.strip() != ''], key=len)]
