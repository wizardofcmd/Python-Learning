###############################################################################
###                                                                         ###
###                     Simplified Code compared to mine                    ###
###                                                                         ###
###        s = input().strip()                                              ###
###        n = int(input().strip())                                         ###
###        L = len(s)                                                       ###
###        print(s.count('a') * (n//L) + s[:n % L].count('a'))              ###
###############################################################################

def repeated_string(s, n):
    # Substring variable
    infin_string = ''
    # Counter
    counter = 0
    while len(infin_string) < n:
        infin_string += s
    if len(infin_string) > n:
        # Variable to remove extra characters, depending on length difference
        diff = len(infin_string) - n
        infin_string = infin_string[:-diff]

    for char in infin_string:
        if char == 'a':
            counter += 1
    print(infin_string)
    print(counter)

# String for infinite use
s = 'gfcaaaecbg'
# Number of characters in infinite substring
n = 547602

repeated_string(s, n)
