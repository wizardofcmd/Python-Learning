# a, being the list of integers
# d, being the number of times to rotate left
def rotLeft(a, d):
    i = 0
    while i < d:
        for x in range(len(a)):
            a[1] = a[x]
        i += 1
    return a

a = [1, 2, 3, 4, 5]
d = 2
result = rotLeft(a, d)
print(result)
