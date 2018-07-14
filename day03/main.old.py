import itertools

def right(x, y):
    return x + 1,  y

def up(x, y):
    return x, y + 1

def left(x, y):
    return x - 1, y

def down(x, y):
    return x, y - 1

def spiral(last_num):
    num = 1
    coord = 0, 0
    spiral_size = 1

    mov = itertools.cycle([right, up, left, down])
    spiral = [(num, coord)]
    
    while True:
        for _ in range(2):
            turn = next(mov)
            for _ in range(spiral_size):
                if num >= last_num:
                    n, m = spiral[-1][1]
                    return abs(n) + abs(m)
                coord = turn(*coord)
                num +=1
                spiral.append((num, coord))
        # the spiral_size increments every 2 direction changes
        spiral_size += 1

print(spiral(325489))
