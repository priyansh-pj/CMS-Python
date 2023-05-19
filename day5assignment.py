# --------------------------function-----------------------------

#@title Write a Program that counts athe number of vowels in a given word.
class function:
  def fun(str):
    vowels = 0
    for i in str:
      if(i=='a' or i=='e' or i=='i'or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels += 1
    return "Number of Vowels are: ", vowels
  str = input("Enter String: ")
  print(fun(str))

#@title Write a Program that takes a string input and prints its reverse.

  def fun1(str1):
    return str1[::-1]
  str1 = input("Enter String: ")   
  print(fun1(str1))

#@title Write a Program that checks if a given number is prime or not.
  def fun(num ):
    flag = False
    if num == 1:
      return num, "is not a Prime Number"
    elif num > 1:
      for i in range (2,num):
        if(num % i) == 0:
          flag = True
          break
      if flag:
        return num, "is not a Prime Number"
      else:
        return num,"is a Prime Number"
  num = int(input("Enter the umber: "))
  print(fun(num))

#@title Write a Program that calculates the fatorial of a given number.
  def fun(num):
    
    fac = 1
    if num < 0:
      return "sorry, factorial is not exist for Negetive numbers"
    elif num == 0:
      return "The fatorial of 0 is 1"
    else:
      for i in range (1, num + 1):
        fac *= i
      return "The Fatorial of " ,num, "is ", fac
  num = int(input("Enter the Number: "))
  print(fun(num))
  
  #@title Write a Program that generate a random number and lets the user guess it, providing hints along the way.
import random

def ran(num):  
  guess = None 

  while guess != num:
    guess = int(input("guess a number between 1 to 10: "))

    if guess == num:
      print ("Congratulations! you won! ")
      break
    else:
      print("nope, please try again!")
num = random.randint(1,10)
print (ran(num))

# -----------------------------------class--------------------------------

#@title Write a Program that counts athe number of vowels in a given word.
class function:
  str = input("Enter String: ")
  vowels = 0
  for i in str:
    if(i=='a' or i=='e' or i=='i'or i=='o'or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
      vowels += 1
  
a = function()
print("Number of Vowels are: ", a.vowels)

#@title Write a Program that takes a string input and prints its reverse.
class function1:
  str1 = input("Enter String: ")   
b = function1()
print(b.str1[::-1])

#@title Write a Program that checks if a given number is prime or not.
class function2:
  num = int(input("Enter the Number: "))
  flag = False
  if num == 1:
    print (num, "is not a Prime Number")
  elif num > 1:
    for i in range (2,num):
      if(num % i) == 0:
        flag = True
        break
    if flag:
      print (num, "is not a Prime Number")
    else:
      print (num,"is a Prime Number")
function2()

#@title Write a Program that calculates the fatorial of a given number.
class function3:
  num = int(input("Enter the Number: "))
  fac = 1
  if num < 0:
    "sorry, factorial is not exist for Negetive numbers"
  elif num == 0:
    "The fatorial of 0 is 1"
  else:
    for i in range (1, num + 1):
      fac *= i
    "The Fatorial of " ,num, "is ", fac
d = function3()
print (d.fac)

#@title Write a Program that generate a random number and lets the user guess it, providing hints along the way.
import random

class function4: 
  num = random.randint(1,10)
  guess = None 

  while guess != num:
    guess = int(input("guess a number between 1 to 10: "))

    if guess == num:
      print ("Congratulations! you won! ")
      break
    else:
      print("nope, please try again!")
function4()

# ---------------------------------iteration--------------------------------
#@title program of iteration

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(10)

i = iter(numbers)

for _ in range(1, 11):
  print(next(i)) 
