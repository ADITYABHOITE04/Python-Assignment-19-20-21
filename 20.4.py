
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