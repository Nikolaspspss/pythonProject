

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



def win_v1 (f,user):
    def chek_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line (f[n][0], f[n][1], f[n][2], user) or \
        chek_line(f[1][n], f[1][n], f[1][n], user) or \
        chek_line(f[0][0], f[1][1], f[2][2], user) or \
        chek_line(f[2][0], f[1][1], f[0][2], user):
            return True
    return False

def win_v2(f, user):
    win_cord=(((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,2),(1,1),(2,0)), \
             ((0, 0), (1, 1), (2, 2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2))),
    for cord in win_cord:
        symbles=[]
        for c in cord:
            symbles.append(f[c[0]][c[1]])
            if symbles == [user, user, user]:
                return True
        return False

def win_v3(f,user):
    f_list=[]
    for i in f:
        f_list+=1
    positions=[[0,1,2][3,4,5][6,7,8][0,3,6][1,4,7][2,5,8][0,4,8][2,4,6]]
    indeces=set([i for i,x in enumerate(f_list) if x==user])
    for p in  positions:
        if len(indeces.intersection((set(p))))==3:
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

