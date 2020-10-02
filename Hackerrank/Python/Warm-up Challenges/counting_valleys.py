def countingValleys(steps, path):
    valleyPassed = 0
    # Sea level is set to 0
    level = 0
    for n in range(steps):
        if path[n] == 'U':
            if level + 1 == 0:
                valleyPassed += 1
            level += 1
        elif path[n] == 'D':
            level -= 1
    return valleyPassed

path = "DUDUDUDU"
steps = 8
result = countingValleys(steps, path)
print(result)
