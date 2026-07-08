multiply = lambda a, b: (a * 3, b * 3)
def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Output :", multiply(num1, num2))

if __name__ == "__main__":
    main()