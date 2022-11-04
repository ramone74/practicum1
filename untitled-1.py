def CheckWin(a, player):
    f = False
    for i in range(len(a) - 2):
        for j in range(len(a[i]) - 2):
            if a[i][j]:
                if ((a[i][j + 1]) and a[i][j + 2]) or ((a[i + 1][j]) and a[i + 2][j]) or (a[i + 1][j + 1] and a[i + 2][j + 2]):
                    print("Игрок 1 победил" if player else "Игрок 2 победил")
                    f = True
                    


a = [[0] * 10 for j in range(10)]
player = 0
while True:
    if player == 0:
        print("Игрок 1, введите клетку на которую вы хотите поставить фишку")
    else:
        print("Игрок 2, введите клетку на которую вы хотите поставить фишку")
    x, y = map(int, input().split())
    if x > 10 or x < 1 or y > 10 or y < 1:
        print("Поле неккоректно, введите другое")
        continue
    if a[x - 1][y - 1] == 1:
        print("На этом поле уже есть фишка, введите другое поле")
        continue
    else:
        a[x - 1][y - 1] = 1
    for i in range(10):
        for j in range(10):
            print(a[i][j], end="  "),
        print("\n")
    if f:
        break
    if player == 0:
        player = 1
    else:
        player = 0