
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