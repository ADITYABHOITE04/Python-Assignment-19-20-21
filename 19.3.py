from functools import reduce


def main():
    size  =  int(input("Enter the number of elements : "))

    data = []

    for i in range(size):
        value = int(input())
        data.append(value)

    fdata = list(filter(lambda no: 70 <= no <= 90, data))

    mdata = list(map(lambda no: no + 10, fdata))

    if mdata:
        answer = reduce(lambda a, b: a * b, mdata)
    else:
        answer = 0

    print("List after filter :", fdata)
    print("List after map :", mdata)
    print("Output of reduce :", answer)

if __name__ == "__main__":
    main()