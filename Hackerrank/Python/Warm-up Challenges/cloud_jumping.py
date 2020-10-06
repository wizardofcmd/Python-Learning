###############################################################################
###                                                                         ###
###             Had to look at the editorial for the solution.              ###
###                                                                         ###
###############################################################################

def cloudJumping(c):
    curr = 0
    jumps = 0
    n = len(c)

    while (curr < (n-1)):
        # Making sure no IndexError occurs
        if ((curr+2) < n):
            if (c[curr+2] == 0):
                curr += 1
        curr += 1
        jumps += 1

    print(jumps)

c = [0, 0, 0, 1, 0, 0]
cloudJumping(c)
