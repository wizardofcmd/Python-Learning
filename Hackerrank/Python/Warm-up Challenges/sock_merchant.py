###############################################################################
### One solution I found on Hackerrank basically turned all that            ###
### code into a pile of mush:                                               ###
###                                                                         ###
### return sum([ar.count(i)//2 for i in set(ar)])                           ###
###############################################################################

def sockMerchant(ar):
    pair = 0
    # Setting n to be the set of numbers that exist in ar
    for n in set(ar):
        # If there's 2 or more socks that match but there's an uneven amount
        if ar.count(n) >= 2 and ar.count(n) % 2 != 0:
            pair += int(ar.count(n)/2)
        # If there's 2 or more socks that match and all can be made into pairs
        if ar.count(n) >= 2 and ar.count(n) % 2 == 0:
            pair += int(ar.count(n)/2)
        # Simply continues the loop if there's only one sock
        if ar.count(n) == 1:
            continue
    return pair

ar = []
active = True

print('Matching socks! Type \'stop\' to stop entering integers.')
while active:
        num = input('Enter a number: ')
        if num.lower() == 'stop':
            active = False
        else:
            ar.append(num)

pairs = sockMerchant(ar)
print(pairs)
