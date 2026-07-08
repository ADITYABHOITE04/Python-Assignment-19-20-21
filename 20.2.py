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