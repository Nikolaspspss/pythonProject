field = [['-']*3 for _ in range(3)]
while True:
    count = 0
    if count == 9:
        break
    if count%2 == 0:
        count += 1
        show_field(field)
        x,y = user_input(field)
        field[x][y] = 'x'
        print('Количество ходов', count)
    if count%1 == 0:
        count += 1
        show_field(field)
        x,y = user_input(field)
        field[x][y] = 'o'
        print('Количество ходов', count)

