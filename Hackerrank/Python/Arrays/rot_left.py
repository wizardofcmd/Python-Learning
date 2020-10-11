# a, being the list of integers
# d, being the number of times to rotate left
def rotLeft(a, d):
    return a[-d % len(a):] + a[:-d % len(a)]

a = [1, 2, 3, 4, 5]
d = 4
result = rotLeft(a, d)
print(result)
