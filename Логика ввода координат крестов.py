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