field = [['-']*3 for _ in range(3)]

print(field)

def show_field(field):
    print('   0  1  2')
    for i in range(len(field)):
        print(str(i) + '  ' + '  '.join(field[i]))

show_field(field)