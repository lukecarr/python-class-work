from datetime import datetime
import time
import random
import urllib.request
import json

class QuickExercises():
    def task1():
        print("Number of Characters: " + str(len(input("String to count: "))))
    def task2():
        print("Word Reversed: " + input("Word to Reverse: ")[::-1])
    def round(number):
        if number % 1 >= 0.5:
            return int(number + (1 - (number % 1)))
        else:
            return int(number // 1)
    def task3():
        userString = input("5 Letter String: ")
        sum = ord(userString[0]) + ord(userString[1]) + ord(userString[2]) + ord(userString[3]) + ord(userString[4])
        print("Average Letter: " + chr(Exercises.round(sum / 5)))
    def task4():
        chars = list(input("5 Letter String: "))
        frequencies = dict.fromkeys(sorted(set(chars), key=chars.index), 0)
        if len(frequencies) == 1:
            frequencies[list(frequencies.keys())[0]] = 5
        elif len(frequencies) == 2:
            element1 = list(frequencies.keys())[0]
            frequencies[element1] = chars.count(element1)
            element2 = list(frequencies.keys())[1]
            frequencies[element2] = chars.count(element2)
        elif len(frequencies) == 3:
            element1 = list(frequencies.keys())[0]
            frequencies[element1] = chars.count(element1)
            element2 = list(frequencies.keys())[1]
            frequencies[element2] = chars.count(element2)
            element3 = list(frequencies.keys())[2]
            frequencies[element3] = chars.count(element3)
        elif len(frequencies) == 4:
            element1 = list(frequencies.keys())[0]
            frequencies[element1] = chars.count(element1)
            element2 = list(frequencies.keys())[1]
            frequencies[element2] = chars.count(element2)
            element3 = list(frequencies.keys())[2]
            frequencies[element3] = chars.count(element3)
            element4 = list(frequencies.keys())[3]
            frequencies[element4] = chars.count(element4)
        else:
            element1 = list(frequencies.keys())[0]
            frequencies[element1] = chars.count(element1)
            element2 = list(frequencies.keys())[1]
            frequencies[element2] = chars.count(element2)
            element3 = list(frequencies.keys())[2]
            frequencies[element3] = chars.count(element3)
            element4 = list(frequencies.keys())[3]
            frequencies[element4] = chars.count(element4)
            element5 = list(frequencies.keys())[4]
            frequencies[element5] = chars.count(element5)
        print(frequencies)
    def task4iter():
        chars = list(input("x Letter String: "))
        frequencies = dict.fromkeys(sorted(set(chars), key=chars.index), 0)
        for key in frequencies.keys():
            frequencies[key] = chars.count(key)
        print(frequencies)

class Exercises():
    def task1():
        inputtedString = input("String to Process: ")
        if len(inputtedString) < 2:
            response = ""
        else:
            response = inputtedString[0:2] + inputtedString[-2:]
        print(response)
    def task2():
        inputtedString = input("String to Process: ")
        print(inputtedString[0] + inputtedString.replace(inputtedString[0], "$")[1:])
    def task3():
        currentYear = datetime.now().year
        if (currentYear % 4 == 0 and currentYear % 100 != 0) or currentYear % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    def task4():
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    def task5():
        print("How long do you think 1 second is? Press ENTER when you think it has been 1 second.\n\nStarting from...")
        time.sleep(2)
        print("Now!")
        startTime = time.time()
        input("")
        score = abs(1 - (time.time() - startTime))
        print("Your score: " + str(score) + " seconds")

class ReactionGame():
    def __init__(self):
        self.leaderboard = {}
    def load_leaderboard(self):
        with urllib.request.urlopen("https://api.myjson.com/bins/1fc2av") as url:
            data = json.loads(url.read().decode())
            self.leaderboard = data
    def save_leaderboard(self):
        req = urllib.request.Request("https://api.myjson.com/bins/1fc2av", method="PUT", data=json.dumps(self.leaderboard).encode('utf8'), headers={'Content-type': 'application/json'})
        urllib.request.urlopen(req)
    def add_player_score(self, username, score):
        if username in list(self.leaderboard.keys()):
            return False
        self.leaderboard[username] = score
    def check_username(self, username):
        for usernames in list(self.leaderboard.keys()):
            if usernames.lower().strip() == username.lower().strip():
                return True
        return False
    def gameloop(self):
        self.load_leaderboard()
        while True:
            username = input("Username (case insensitive): ").strip()
            while self.check_username(username):
                print("Username taken!")
                username = input("Username (case insensitive): ").strip()
            print("When you see the phrase 'HELLO WORLD' appear press enter as quick as possible!")
            print("The delay before the message appears is randomised each time to prevent cheating.")
            time.sleep(2)
            print("Get Ready!")
            time.sleep(random.randint(3,9))
            startTime = time.time()
            print("HELLO WORLD")
            input("")
            score = (time.time() - startTime)
            print("Your score: " + str(score) + " seconds")
            self.add_player_score(username, score)
            self.save_leaderboard()
            for index, (key, value) in enumerate(self.leaderboard.items()):
                if index > 9:
                    break
                print(str(index+1) + ". " + str(key) + ": " + str(value))
            print("\n\nStart Again?")
            response = input("Yes (y) to continue or otherwise to cancel? ").lower().strip()
            if response == "y":
                continue
            else:
                break
