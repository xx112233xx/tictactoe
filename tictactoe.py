def check(a, b, c, ch):
    if a.count(ch) == 3 or b.count(ch) == 3 or c.count(ch) == 3:
        return 1
    elif a[0] == b[0] == c[0] == ch or a[1] == b[1] == c[1] == ch or a[2] == b[2] == c[2] == ch:
        return 1
    elif a[0] == b[2] == c[2] == ch or a[2] == b[1] == c[0] == ch:
        return 1


def display(a, b, c):
    print("-" * 9)
    print(f"| {a[0]} {a[1]} {a[2]} |")
    print(f"| {b[0]} {b[1]} {b[2]} |")
    print(f"| {c[0]} {c[1]} {c[2]} |")
    print("-" * 9)


# print("Enter cells: > ")
# str_line = input()
str_line = ' ' * 9
field = list(str_line[0:3]), list(str_line[3:6]), list(str_line[6:])
display(field[0], field[1], field[2])
n = 0
while n < 9:
    print("Enter coordinates: > ")
    cord = input().split()
    col = int(cord[0])-1
    row = int(cord[1])-1
    if row == 0:
        row = 2
    elif row == 2:
        row = 0
    if not (-1 < row < 3) or not (-1 < col < 3):
        print("Coordinates should be from 1 to 3!")
    elif not str(col).isdigit() or not str(row).isdigit():
        print("You should enter numbers!")
    elif field[row][col] == 'X' or field[row][col] == 'O':
        print("This cell is occupied! Choose another one!")
    else:
        n += 1
        field[row][col] = 'X'
        display(field[0], field[1], field[2])
        xWin = check(field[0], field[1], field[2], 'X')
        oWin = check(field[0], field[1], field[2], 'O')
        if str_line.count('X') > str_line.count('O') + 1 or str_line.count('O') > str_line.count('X') + 1:
            print("Impossible")
        elif oWin and xWin:
            print("Impossible")
        elif xWin and not oWin:
            print("X wins")
        elif oWin and not xWin:
            print("O wins")
        elif str_line.count('X') + str_line.count('O') != 9 and not (xWin or oWin):
            print("Game not finished")
        else:
            print("Draw")



