import itertools

def spiral(last_num):
    num = 1
    spiral_size = 1
    coord = 0, 0
    mov = itertools.cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])
    downward_spiral = [(num, coord)]
    
    while True:
        for _ in range(2):
            turn = next(mov)
            for _ in range(spiral_size):
                if num >= last_num:
                    n, m = downward_spiral[-1][1]
                    return abs(n) + abs(m)
                coord = (coord[0] + turn[0], coord[1] + turn[1])
                num += 1
                downward_spiral.append((num, coord))
        # the spiral_size increments every 2 direction changes
        spiral_size += 1

print(spiral(325489))
