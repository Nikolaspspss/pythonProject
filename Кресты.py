

field = [['-']*3 for _ in range(3)]

def show_field(field):
    print('   0  1  2')
    for i in range(len(field)):
        print(str(i) + '  ' + '  '.join(field[i]))

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



def win_v1 (field,user):
    def chek_line(a1, a2, a3, user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line (field[n][0], field[n][1], field[n][2], user) or \
        chek_line(field[1][n], field[1][n], field[1][n], user) or \
        chek_line(field[0][0], field[1][1], field[2][2], user) or \
        chek_line(field[2][0], field[1][1], field[0][2], user):
            return True
    return False


while True:
    if count > 9:
        print('Ничья')
        break
    if count%2 == 0:
        user = 'X'
    else:
        user = 'O'
    show_field(field)
    x,y=user_input(field)
    field[x][y]=user
    count+=1
    if win_v1(field,user):
        print(f'viktory {user}')
        show_field(field)
        break
    print('количество ходов',count)