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