from time import time
from datetime import datetime
from random import getrandbits

def xFactorOfY(x, y):
  return y % x == 0

def countUpperAndLower(string):
  return (len([char for char in string if 65 <= ord(char) <= 90]), len([char for char in string if 97 <= ord(char) <= 122]))

def reverse(string):
  return string[::-1]

def isPrimeEfficient(x):
  return not (x < 2 or any(x % y == 0 for y in range(2, int(x ** 0.5) + 1)))

def isPrime(x):
  if x == 1: return False
  for y in range(2, int(x/2)+1):
    if x % y == 0:
      return False
  return True

def isPrimeInefficient(x):
  for y in range(2, x):
    if x % y == 0:
      return False
  return True

def getFactors(x):
  return [y for y in range(1, int(x/2)+1) if x % y == 0]

def isPerfect(x):
  return sum(getFactors(x)) == x

def generatePrime():
  start = getrandbits(128)
  if start % 2 == 0:
    start += 1
  while not isPrimeEfficient(start):
    start += 2
  return start
