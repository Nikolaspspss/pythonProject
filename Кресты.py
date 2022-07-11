

field = [['-']*3 for _ in range(3)]

def show_field(field):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i) + ' ' + ' '.join(field[i]))

show_field(field)

#i = 1
#j = 2
#print(i+j)

def user_input(f):
    while True:
        place= input('введите координаты :').split()
        if len(place)!=2:
            print("введите две координаты")
            continue
        break
        if  not(place[0].isdigit() and place[1].isdigit()):
            print('введите числа')
            сontinue
        x,y = map(int,place)
        if not(x>=0 and x<3 and y<3 and y>=0):
            print('вышли из диапозона')
            сontinue
        if f[x][y]!='-':
            print('клетка занята')
            continue
        break
        return x,y
user_input(field)