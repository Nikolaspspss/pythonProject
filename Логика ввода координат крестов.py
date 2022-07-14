
def user_input(field):
    while True:
        place= input('введите координаты :').split()
        if len(place)!=2:
            print("введите две координаты")
            continue
        if  not(place[0].isdigit() and place[1].isdigit()):
            print('введите числа')
            continue
        x,y = map(int,place)
        if field [x][y] != '-':
            print('клетка занята')
            continue
        if not(3>=x>=0 and 3>=y>=0 ):
            print('Вышли из диапозона')
            continue
        break
    return x,y