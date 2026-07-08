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