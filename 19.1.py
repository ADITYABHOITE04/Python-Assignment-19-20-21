power = lambda no1, no2: (no1 ** 2, no2 ** 2)
def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Output is :", power(num1, num2))

if __name__ == "__main__":
    main()