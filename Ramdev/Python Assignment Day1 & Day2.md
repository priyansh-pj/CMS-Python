```python
var_a =1
print(var_a)
print(type(var_a))

b = 2.5
print(b)
print(type(b))

c="Ramdev"
print(c)
print(type(c))

d = ["apple","cherry",1]
print(d)
print(type(d))

g = {1,2,3}
print(g)
print(type(g))

f = ("herry","pranjal")
print(f)
print(type(f))

r = {"name":"pranjal",
     "branch":"CSE-IML","semester": 4}
print(r)
print(type(r))

x =3+7j
print(x)
print(type(x))

print("Hello",end="-")
print("World")


```

    1
    <class 'int'>
    2.5
    <class 'float'>
    Ramdev
    <class 'str'>
    ['apple', 'cherry', 1]
    <class 'list'>
    {1, 2, 3}
    <class 'set'>
    ('herry', 'pranjal')
    <class 'tuple'>
    {'name': 'pranjal', 'branch': 'CSE-IML', 'semester': 4}
    <class 'dict'>
    (3+7j)
    <class 'complex'>
    Hello-World
    


```python
a = 3
b = 4
if 3<4:
  print("b is greater")
else:
 print("a is greater")
```

    b is greater
    

# count vowels in word


```python
String = input('Enter the string :')
count = 0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))

```

    Enter the string :Ramdev Lodhi
    Total vowels are :4
    


```python
txt = input("enter string:")
print(txt [::-1])

```

    enter string:vedmaR
    Ramdev
    


```python
num =int(input("enter the no."))
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
```

    enter the no.17
    17 is a prime number
    


```python
def factorial():

    factorial = 1    
    if num < 0:    
        print(" Factorial does not exist for negative numbers")    
    elif num == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1,num + 1):    
            factorial = factorial*i    
            print("The factorial of",num,"is",factorial)
num = int(input("Enter a number: "))    
print(factorial())
```

    Enter a number: 5
    The factorial of 5 is 1
    The factorial of 5 is 2
    The factorial of 5 is 6
    The factorial of 5 is 24
    The factorial of 5 is 120
    None
    


```python
import random
random_number = random.randint(1,100)
print("random number:",random_number)
```

    random number: 77
    

# Programe By defining the function



```python
def count_vowels(word):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in word:
        if char in vowels:
            vowel_count += 1
    return vowel_count

word = input("Enter a word: ")
result = count_vowels(word)
print("Number of vowels:", result)

def reverse_string(input_string):
    return input_string[::-1]

word = input("Enter a string: ")
result = reverse_string(word)
print("Reversed string:", result)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")
    
def factorial(number):
    if number < 0:
        return None
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
result = factorial(number)
if result is None:
    print("Factorial cannot be calculated for negative numbers.")
else:
    print("Factorial of", number, "is", result)
    
import random

def guess_number(secret_number):
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed the number", secret_number, "in", attempts, "attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

secret_number = random.randint(1, 10)

print("I have chosen a number between 1 and 10.")
print("Can you guess it?")

guess_number(secret_number)
```

    Enter a word: Ramdev Lodhi
    Number of vowels: 4
    Enter a string: vedmaR
    Reversed string: Ramdev
    Enter a number: 17
    17 is a prime number.
    Enter a number: 5
    Factorial of 5 is 120
    I have chosen a number between 1 and 10.
    Can you guess it?
    Enter your guess: 4
    Too low. Try again.
    Enter your guess: 7
    Too low. Try again.
    Enter your guess: 10
    Too high. Try again.
    Enter your guess: 9
    Congratulations! You guessed the number 9 in 4 attempts.
    


```python

class VowelCounter:
    def __init__(self, word):
        self.word = word.lower()
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def count_vowels(self):
        count = 0
        for char in self.word:
            if char in self.vowels:
                count += 1
        return count
word = input("enter a word: ")
counter=VowelCounter(word)
vowel_count = counter.count_vowels()
print("Number of vowels: ",vowel_count)
```

    enter a word: ramdev lodhi
    Number of vowels:  4
    


```python
class Stringreverser:
    def __init__(self,word):
        self.word = word
      

    def reverse_string(self):
        reversed_string = self.word[::-1]
        return reversed_string

word = input("Enter a string: ")
reverser = Stringreverser(word)
reversed_string = reverser.reverse_string()
print("Reversed string:", reversed_string )
```

    Enter a string: ram
    Reversed string: mar
    


```python
class Primechecker:
    def __init__(self,num):
        self.num = num
    def is_prime(self):
        if self.num <=1:
            return False
        for i in range(2, int(self.num/2) + 1):
            if self.num % i == 0:
                return False
        return True

num = int(input("Enter a number: "))
x = Primechecker(num)
is_prime = x.is_prime()
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
```

    Enter a number: 17
    17 is a prime number.
    


```python
class Data: 
      def function(self):
        print("hello world")
var = Data()  
var.function()
```

    hello world
    


```python
class FactorialCalculator:
    def calculate_factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.calculate_factorial(number - 1)


calculator = FactorialCalculator()
number = int(input("Enter a number: "))
factorial = calculator.calculate_factorial(number)
print("The factorial of", number, "is", factorial)
```

    Enter a number: 5
    The factorial of 5 is 120
    
