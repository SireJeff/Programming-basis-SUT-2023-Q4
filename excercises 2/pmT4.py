def move_left(i, n):
    return max(0, i - 1)

def move_right(i, n):
    return min(n - 1, i + 1)

def move_down(j):
    return j + 1

def print_maze(map1, n, i):
    last_row = next((row for row in reversed(map1) if '*' in row), None)
    
    if last_row:
        last_index = len(map1) - map1[::-1].index(last_row) - 1
        for row in map1[:last_index + 1]:
            print(" ".join(row))
    else:
        for row in map1:
            print(" ".join(row))
    
    if i != n - 1:
        print("There's no way out!")

def run_commands(map1, n, commands):
    i, j = 0, 0
    map1[j][i] = '*'

    for command in commands:
        if command == "L":
            i = move_left(i, n)
        elif command == "R":
            i = move_right(i, n)
        elif command == "B":
            j = move_down(j)
        map1[j][i] = '*'

    return i
n = int(input())
row = ['.'] * n
map1 = [row.copy() for _ in range(1000)]
commands = []
command_input = input()
while command_input != "END":
    commands.append(command_input)
    command_input = input()
last_position = run_commands(map1, n, commands)
print_maze(map1, n, last_position)