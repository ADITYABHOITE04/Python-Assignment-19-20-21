# Python Assignments
---
## Student Details
Name:Aditya Bhoite

*Student ID:* 182
---
# Assignment 19
---

### Question 1

Write a program which contains one lambda function which accepts one parameter and returns the power of two.

### Answer

```python
power = lambda no1, no2: (no1 ** 2, no2 ** 2)
def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Output is :", power(num1, num2))

if __name__ == "__main__":
    main()
```

### Output

<img width="475" height="106" alt="Screenshot 2026-07-08 192649" src="https://github.com/user-attachments/assets/a938f007-c663-4e20-8a16-bb4eb34275a1" />

---

### Question 2

Write a program which contains one lambda function which accepts two parameters and returns its multiplication.

### Answer

```python
multiply = lambda a, b: (a * 3, b * 3)
def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Output :", multiply(num1, num2))

if __name__ == "__main__":
    main()
```

### Output
<img width="440" height="107" alt="Screenshot 2026-07-08 193211" src="https://github.com/user-attachments/assets/66f98607-fe5e-41e9-b977-ca5041f900af" />


---

### Question 3

Write a program which contains filter(), map() and reduce().

Accept a list from the user.

Filter the numbers which are greater than or equal to 70 and less than or equal to 90.

Map function should increase each number by 10.

Reduce function should return the multiplication of all numbers.

### Answer
```python
from functools import reduce


def main():
    size  =  int(input("Enter the number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    fdata = list(filter(lambda no: 70 <= no <= 90, data))

    mdata = list(map(lambda no: no + 10, fdata))

    if mdata:
        answer = reduce(lambda a, b: a * b, mdata)
    else:
        answer = 0

    print("List after filter :", fdata)
    print("List after map :", mdata)
    print("Output of reduce :", answer)

if __name__ == "__main__":
    main()
```

### Output

<img width="515" height="249" alt="Screenshot 2026-07-08 195023" src="https://github.com/user-attachments/assets/6d6f38aa-63e2-4581-b0ef-cd1e448fe85b" />


---

### Question 4

Write a program which contains filter(), map() and reduce().

Accept a list from the user.

Filter all even numbers.

Map function should calculate the square of each number.

Reduce function should return the addition of all numbers.

### Answer

```python
from functools import reduce

size = int(input("How many numbers : "))

data = []

for i in range(size):
    value = int(input())
    data.append(value)

fdata = list(filter(lambda no: no % 2 == 0, data))

mdata = list(map(lambda no: no * no, fdata))

answer = reduce(lambda a, b: a + b, mdata)

def main():
    size = int(input("How many numbers : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    fdata = list(filter(lambda no: 70 <= no <= 90, data))

    mdata = list(map(lambda no: no + 10, fdata))

    if mdata:
        answer = reduce(lambda a, b: a * b, mdata)
    else:
        answer = 0

print("List after filter :", fdata)
print("List after map :", mdata)
print("Output of reduce :", answer)

if __name__ == "__main__":
    main()
```

### Output

<img width="578" height="229" alt="Screenshot 2026-07-08 195313" src="https://github.com/user-attachments/assets/ff139a72-46ad-4090-b8b8-e3265d62af0b" />


---

### Question 5

Write a program which contains filter(), map() and reduce().

Accept a list from the user.

Filter all prime numbers.

Map function should multiply each number by 2.

Reduce function should return the maximum number.

### Answer
```python
from functools import reduce

def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


size = int(input("How many numbers : "))

data = []

for i in range(size):
    value = int(input())
    data.append(value)

fdata = list(filter(CheckPrime, data))

mdata = list(map(lambda no: no * 2, fdata))

answer = reduce(lambda a, b: a if a > b else b, mdata)

print("List after filter :", fdata)
print("List after map :", mdata)
print("Output of reduce :", answer)
```

### Output

<img width="489" height="221" alt="Screenshot 2026-07-08 195651" src="https://github.com/user-attachments/assets/276ee948-177f-444a-af97-3f680e158983" />


---

# Assignment 20

---

### Question 1

Design a Python application that creates two threads named Even and Odd.

Even thread should display the first 10 even numbers.

Odd thread should display the first 10 odd numbers.

### Answer

```python
import threading

def main():
    pass

def Even():
    print("Even Numbers :")
    for i in range(2, 10, 2):
        print(i)

def Odd():
    print("Odd Numbers :")
    for i in range(1, 10, 2):
        print(i)

t1 = threading.Thread(target=Even)
t2 = threading.Thread(target=Odd)

t1.start()
t2.start()

t1.join()
t2.join()

if __name__ == "__main__":
    main()
```


### Output

<img width="495" height="298" alt="Screenshot 2026-07-08 200658" src="https://github.com/user-attachments/assets/69afaced-cc59-4ea2-ad53-c3f554b89faf" />


---

### Question 2

Design a Python application that creates two threads named EvenFactor and OddFactor.

Both threads should accept one integer.

EvenFactor thread should display all even factors and their sum.

OddFactor thread should display all odd factors and their sum.

Main thread should display "Exit from main".

### Answer
```python
import threading

def EvenFactor(no):
    sum = 0

    print("Even Factors :")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i)
            sum = sum + i

    print("Sum of Even Factors :", sum)

def OddFactor(no):
    sum = 0

    print("Odd Factors :")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i)
            sum = sum + i

    print("Sum of Odd Factors :", sum)

num = int(input("Enter number : "))

t1 = threading.Thread(target=EvenFactor, args=(num,))
t2 = threading.Thread(target=OddFactor, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Exit from main")
```

### Output

<img width="491" height="188" alt="Screenshot 2026-07-08 202000" src="https://github.com/user-attachments/assets/2b6fdb3b-2fe7-41ce-aa5c-02c735b0757c" />



---

### Question 3

Design a Python application that creates two threads named EvenList and OddList.

Accept a list from the user.

EvenList thread should display all even numbers and their sum.

OddList thread should display all odd numbers and their sum.

### Answer

```python
import threading

def EvenList(data):
    sum = 0

    print("Even Numbers :")

    for i in data:
        if i % 2 == 0:
            print(i)
            sum = sum + i

    print("Sum of Even Numbers :", sum)

def OddList(data):
    sum = 0

    print("Odd Numbers :")

    for i in data:
        if i % 2 != 0:
            print(i)
            sum = sum + i

    print("Sum of Odd Numbers :", sum)

size = int(input("Enter number of elements : "))

data = []

for i in range(size):
    value = int(input("Enter number : "))
    data.append(value)

t1 = threading.Thread(target=EvenList, args=(data,))
t2 = threading.Thread(target=OddList, args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()
```

### Output

<img width="473" height="230" alt="Screenshot 2026-07-08 202102" src="https://github.com/user-attachments/assets/18fabea4-a865-4583-ab50-a41c9288d031" />


---

### Question 4

Design a Python application that creates three threads named Small, Capital and Digits.

Accept a string from the user.

Small thread should count lowercase letters.

Capital thread should count uppercase letters.

Digits thread should count numeric digits.

Display Thread ID and Thread Name.

### Answer
```python

import threading

def main():
    pass

def Small(text):
    count = 0

    for ch in text:
        if ch.islower():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Small letters :", count)

def Capital(text):
    count = 0

    for ch in text:
        if ch.isupper():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Capital letters :", count)

def Digits(text):
    count = 0

    for ch in text:
        if ch.isdigit():
            count = count + 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)

text = input("Enter string : ")

t1 = threading.Thread(target=Small, args=(text,), name="Small")
t2 = threading.Thread(target=Capital, args=(text,), name="Capital")
t3 = threading.Thread(target=Digits, args=(text,), name="Digits")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

if __name__ == "__main__":
    main()
```
### Output

<img width="468" height="155" alt="Screenshot 2026-07-08 202151" src="https://github.com/user-attachments/assets/03f215d2-6084-47d5-9e34-5714976e0b19" />


---

### Question 5

Design a Python application that creates two threads.

Thread1 should display numbers from 1 to 50.

Thread2 should display numbers from 50 to 1.

Execute Thread2 only after Thread1 completes.

### Answer
```python

import threading

def main():
    pass


def Thread1():
    print(f"Thread1 Numbers is :")

    for i in range(1, 51):
        print(i)

def Thread2():
    print(f"Thread2 Numbers is :")

    for i in range(50, 0, -1):
        print(i)

t1 = threading.Thread(target=Thread1)
t2 = threading.Thread(target=Thread2)

t1.start()
t1.join()

t2.start()
t2.join()

if __name__ == "__main__":
    main()
```



### Output

<img width="417" height="470" alt="Screenshot 2026-07-08 212821" src="https://github.com/user-attachments/assets/527823f2-51af-47a0-ba4d-9fbbd8d6c596" />


---

# Assignment 21

### Question 1

Design a Python application that creates two threads named Prime and NonPrime.

Accept a list of integers.

Prime thread should display all prime numbers.

NonPrime thread should display all non-prime numbers.

### Answer
```python
import threading

def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True

def Prime(data):
    print("Prime Numbers :")
    for i in data:
        if CheckPrime(i):
            print(i)

def NonPrime(data):
    print("Non Prime Numbers :")
    for i in data:
        if not CheckPrime(i):
            print(i)

size = int(input("Enter number of elements : "))

data = []

for i in range(size):
    value = int(input("Enter number : "))
    data.append(value)

t1 = threading.Thread(target=Prime,args=(data,))
t2 = threading.Thread(target=NonPrime,args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()
```

### Output

<img width="470" height="223" alt="Screenshot 2026-07-08 214127" src="https://github.com/user-attachments/assets/2f602fb0-d0be-4b75-92c0-5c494ba7ff8a" />

---

### Question 2

Design a Python application that creates two threads.

One thread should display the maximum element.

Another thread should display the minimum element from the list.

### Answer
```python
import threading

def Maximum(data):
    print("Maximum Number :", max(data))

def Minimum(data):
    print("Minimum Number :", min(data))

size = int(input("Enter number of elements : "))

data = []

for i in range(size):
    value = int(input("Enter number : "))
    data.append(value)

t1 = threading.Thread(target=Maximum,args=(data,))
t2 = threading.Thread(target=Minimum,args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()
```

### Output

<img width="449" height="134" alt="Screenshot 2026-07-08 214148" src="https://github.com/user-attachments/assets/682da1ab-e6d7-47a4-8328-7a9ba84d2873" />


---

### Question 3

Design a Python application where multiple threads update a shared variable.

Use Lock to synchronize access.

Display the final value of the shared variable.

### Answer
```python
import threading

counter = 0

lock = threading.Lock()

def Increment():
    global counter

    for i in range(100000):
        lock.acquire()
        counter = counter + 1
        lock.release()

t1 = threading.Thread(target=Increment)
t2 = threading.Thread(target=Increment)
t3 = threading.Thread(target=Increment)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Final Counter :", counter)
```

### Output

<img width="467" height="64" alt="Screenshot 2026-07-08 214231" src="https://github.com/user-attachments/assets/3cea42e6-728b-4053-8a8d-60fc11389d0f" />

---

### Question 10

Design a Python application that creates two threads.

One thread should calculate the sum of all elements.

Another thread should calculate the product of all elements.

Display both results from the main thread.

### Answer
```python
import threading

Sum = 0
Product = 1

def Add(data):
    global Sum

    for i in data:
        Sum = Sum + i

def Multiply(data):
    global Product

    for i in data:
        Product = Product * i

size = int(input("Enter number of elements : "))

data = []

for i in range(size):
    value = int(input("Enter number : "))
    data.append(value)

t1 = threading.Thread(target=Add,args=(data,))
t2 = threading.Thread(target=Multiply,args=(data,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Sum :", Sum)
print("Product :", Product)
```


### Output
<img width="482" height="198" alt="Screenshot 2026-07-08 214305" src="https://github.com/user-attachments/assets/e9897532-0fab-422d-bad7-8b99fa3a6a66" />


---

