

field = [['-']*3 for _ in range(3)]

def show_field(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))

def user_input(field):
    while True:
        place= input('введите координаты :').split()
        if len(place)!=2:
            print("введите две координаты")
            continue
        if  not(place[0].isdigit() and place[1].isdigit()):
            print('введите числа')
            continue
        x,y=map(int,place)
        if not (3>x>=0 and 3>y>=0):
            print('Вышли из диапозона')
            continue
        if field[x][y] != '-':
            print('клетка занята')
            continue
        break
    return x,y
count = 0

def win(f,user):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

while True:
    if count > 9:
        print('Ничья')
        break
    if count%2 == 0:
        user = 'X'
    else:
        user = '0'
    show_field(field)
    x,y=user_input(field)
    field[x][y]=user
    count+=1
    if win(field,user):
        print(f'viktory {user}')
        show_field(field)
    print('количество ходов',count)

