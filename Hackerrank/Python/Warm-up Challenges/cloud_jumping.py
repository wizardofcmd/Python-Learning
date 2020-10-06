def cloudJumping(c):
    curr = 0
    pathLength = 0
    while curr != len(c)-1:
        if curr < len(c)-2 and c[curr+2] == 0:
            curr += 2
        else:
            curr += 1

        pathLength += 1

c = [0, 0, 1, 0, 0, 1, 0]
jumps = cloudJumping(c)
print(jumps)
