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