def cloudJumping(c):
    jumps = 0
    for cloud in range(len(c)):
        if c[cloud] == 1:
            jumps += 1
            continue
        elif c[cloud] == 0:
            try:
                if c[cloud+1] == 0:
                    jumps += 1
                    continue
            except IndexError:
                continue
            jumps += 1
    return jumps


c = [0, 0, 1, 0, 0, 1, 0]
jumps = cloudJumping(c)
print(jumps)
