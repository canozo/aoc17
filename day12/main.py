def solve(pipes, grouped=[], connected_to='0'):
    for line in pipes:
        print(line)
    return len(grouped)


def process_pipes(puzzle):
    result = []
    for line in puzzle:
        pipe, pipes = line.split(' <-> ')
        temp_pipes = [pipe]
        temp_pipes += pipes.split(', ')
        temp_pipes[-1] = temp_pipes[-1].strip()
        result.append(temp_pipes)
    return result


def main():
    with open('example.txt', 'r') as input_file:
        puzzle = input_file.readlines()

    pipes = process_pipes(puzzle)
    part = int(input('part: '))

    if part == 1:
        print(solve(pipes))
    elif part == 2:
        pass


if __name__ == '__main__':
    main()
