M = 8
N = 8


def FloodFilling(screen, a, b, OldColor, NewColor):
    if (a < 0 or a >= M or b < 0 or
            b >= N or screen[a][b] != OldColor or
            screen[a][b] == NewColor):
        return

    screen[a][b] = NewColor

    FloodFilling(screen, a + 1, b, OldColor, NewColor)
    FloodFilling(screen, a - 1, b, OldColor, NewColor)
    FloodFilling(screen, a, b + 1, OldColor, NewColor)
    FloodFilling(screen, a, b - 1, OldColor, NewColor)

def floodFill(screen, a, b, NewColor):
    OldColor = screen[a][b]
    if (OldColor == NewColor):
        return
    FloodFilling(screen, a, b, OldColor, NewColor)


screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

a = 4
b = 4
NewColor = 3
floodFill(screen, a, b, NewColor)

print("After call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end=' ')
    print()
