from functools import reduce


def CheckPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


size = int(input("How many numbers : "))

data = []

for i in range(size):
    value = int(input())
    data.append(value)

fdata = list(filter(CheckPrime, data))

mdata = list(map(lambda no: no * 2, fdata))

answer = reduce(lambda a, b: a if a > b else b, mdata)

print("List after filter :", fdata)
print("List after map :", mdata)
print("Output of reduce :", answer)

