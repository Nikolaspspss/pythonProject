

def winner1 (field, user):
    def chek_line(a1, a2, a3, user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line(field[n][0], field[n][1], field[n][2], user) or \
        chek_line(field[1][n], field[1][n], field[1][n], user) or \
        chek_line(field[0][0], field[1][1], field[2][2], user) or \
        chek_line(field[2][0], field[1][1], field[0][2], user):
            return True
    return False
winner1 (field, user)

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
