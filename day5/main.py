def solve(text):
    steps = 0
    pos = 0
    database = [int(line) for line in text]
    while True:
        if pos < 0 or pos >= len(database):
            break
        steps += 1
        database[pos] += 1
        pos += database[pos] - 1
    return steps


def solve2(text):
    steps = 0
    pos = 0
    database = [int(line) for line in text]
    while True:
        if pos < 0 or pos >= len(database):
            break
        steps += 1
        if database[pos] >= 3:
            database[pos] -= 1
            pos += database[pos] + 1
        else:
            database[pos] += 1
            pos += database[pos] - 1
    return steps

with open('input.txt', 'r') as texto:
    _input = texto.read().split('\n')

print(solve(_input))
print(solve2(_input))
