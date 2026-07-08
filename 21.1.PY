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