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