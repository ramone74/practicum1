#рассмотреть внутренний квадрат размерностью 9, проверять отдельно последние 2 столбца и последние 2 строки
def CheckDiag(a, x, y):
    if a[x + 1][y + 1] or a[x - 1][y - 1] or a[x + 1][y - 1] or a[x - 1][y + 1]:
        return 1
    else:
        return 0
    
def CheckVert(a, x, y):
    if a[x - 1][y] or a[x + 1][y]:
        return 1
    else:
        return 0
    
def CheckHor(a, x, y):
    if a[x][y + 1] or a[x][y - 1]:
        return 1
    else:
        return 0

a = [[0] * 10 for j in range(10)] #заполняем поле нулями
player = 0 #Если значение 0, то ходит игрок 1, а если значение 1, то ходит игрок 2
f = False #флаг победы
#Игроки заполняют поле
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
    #Проверяем есть ли 3 фишки подряд по горизонтали, вертикали и диагонали соответственно
    for i in range(len(a) - 2):
        for j in range(len(a) - 2):
            if a[i][j]:
                if ((a[i][j + 2] and a[i][j + 1]) or (a[i + 1][j] and a[i + 2][j]) or (a[i + 1][j + 1] and a[i + 2][j + 2])):
                    print("Игрок 1 победил" if player else "Игрок 2 победил")
                    f = True
    
    for i in range(len(a) - 1, 1, -1):
        for j in range(len(a) - 1, 1, -1):
            if a[i][j]:
                if ((a[i][j - 2] and a[i][j - 1]) or (a[i - 1][j] and a[i - 2][j]) or (a[i - 1][j - 1] and a[i - 2][j - 2])):
                    print("Игрок 1 победил" if player else "Игрок 2 победил")
                    f = True
    
                
    for i in range(1, len(a) - 1):
        for j in range(1, len(a[i]) - 1):
            #Добавить цикл проверки краев
            if a[i][j] + CheckDiag(a, i, j) + CheckVert(a, i, j) + CheckHor(a, i, j) >= 3:
                print("Игрок 1 победил" if player else "Игрок 2 победил")
                f = True
                #print(a[i][j], CheckDiag(a, i, j), CheckVert(a, i, j), CheckHor(a, i, j))
    #Выводим поле после каждого хода, x - строка, y - столбец
    for i in range(10):
        for j in range(10):
            print(a[i][j], end="  "),
        print("\n", end="")
    if f:
        break
    if player == 0:
        player = 1
    else:
        player = 0