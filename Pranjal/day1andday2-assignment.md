```python
var_a =1
print(var_a)
print(type(var_a))
b = 2.5
print(b)
print(type(b))
c = "pranjal"
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
    pranjal
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
    


```python
b = []
a = int(input("enter element of list"))
for i in range(1,a + 1):
  ele = int(input("entr element:"))
  b.append(ele)
print("largest element is :",max(b))
print("smallest element is :",min(b))
```

    enter element of list3
    entr element:1
    entr element:2
    entr element:3
    largest element is : 3
    smallest element is : 1
    

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

    Enter the string :aioue
    Total vowels are :5
    

# Resvers string


```python
txt = input("enter string:")
print(txt [::-1])

```

    enter string:pranjal
    lajnarp
    

# check prime no.


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

    enter the no.7
    7 is a prime number
    

# check factorial


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
    The factorial of 5 is 120
    None
    

# ramdom no.


```python
import random
random_number = random.randint(1,50)
print("random number:",random_number)

```

    random number: 23
    

# programe by defining the function


```python
def count_vowels(String):
    count = 0
    String = String.lower()
    for i in String:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+=1
    if count == 0:
        return 'No vowels found'
    else:
        return 'Total vowels are :' + str(count)
String = input('Enter the string :')

print(count_vowels(String))
def resvers():

    return (txt [::-1])
txt = input("enter string:")
print(resvers())

def prime():
# If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        return(num, "is not a prime number")
num =int(input("enter the no."))
prime()

def factorial():
    factorial = 1    
    if num < 0:    
        return(" Factorial does not exist for negative numbers")    
    elif num == 0:    
        return("The factorial of 0 is 1")    
    else:    
        for i in range(1,num + 1):    
            factorial = factorial*i    
        print("The factorial of",num,"is",factorial)
num = int(input("Enter a number: "))    
print(factorial())

import random
# Generate a random number between 1 and 5
secret_number = random.randint(1, 5)
attempts = 0
def guess_number(secret_number):
    print("I have chosen a number between 1 and 5.")
print("Can you guess it?")
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

guess_number(secret_number)
    

```


```python
class Vowels_count:
    def __init__(self,string):
        self.string = string.lower()
        self.vowels = ['a','e','i','o','u']
    def count(self):
            count = 0
            for i in self.string:
                if i in self.vowels:
                    count+=1  
            return count
string=input('Enter the string :')
counter=Vowels_count(string) 
count=counter.count()
print("number of vowels:",count)
```

    Enter the string :pranjal
    number of vowels: 2
    


```python
class Resver :
    def __init__(self,input_1):
        self.input_1 = input_1
    def stringreverse(self):
        return(txt [::-1])
txt = input("enter string:")
x = Resver(txt)
y = x.stringreverse()
print("reverse string is :",y)
```

    enter string:pranjal
    reverse string is : lajnarp
    


```python
class prime_number:
    def __init__(self,number):
        self.number = number
    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number/2)+1):
            if self.number % i == 0:
                return False
        return True
num =int(input("enter the no."))
a = prime_number(num)
b = a.is_prime()
if b:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
                
        
```

    enter the no.9
    9 is not a prime number
    


```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
```

    John
    36
    


```python
class Person:
    def __init__(ob_a, name, age):
        ob_a.name = name
        ob_a.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
```

    Hello my name is John
    
