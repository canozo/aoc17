import itertools

# parte 1
suma = 0
with open('input.txt', 'r') as text:
    for line in text.read().split('\n'):
        nums = list(map(int, line.split('\t')))
        suma += max(nums) - min(nums)
print(suma)


# parte 2
suma = 0
with open('input.txt', 'r') as text:
    for line in text.read().split('\n'):
        nums = list(map(int, line.split('\t')))
        for x, y in itertools.combinations(nums, 2):
            if x % y == 0 or y % x == 0:
                suma += x // y + y // x
                break
print(suma)
