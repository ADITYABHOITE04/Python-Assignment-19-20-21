from functools import reduce

size = int(input("How many numbers : "))

data = []

for i in range(size):
    value = int(input())
    data.append(value)

fdata = list(filter(lambda no: no % 2 == 0, data))

mdata = list(map(lambda no: no * no, fdata))

answer = reduce(lambda a, b: a + b, mdata)

def main():
    size = int(input("How many numbers : "))

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