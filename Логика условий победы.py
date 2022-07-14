def winner1 (field, user):
    def chek_line(a1, a2, a3, user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if chek_line(field[n][0], field[n][1], field[n][2], user) or \
        chek_line(field[1][n], field[1][n], field[1][n], user) or\
        chek_line(field[0][0], field[1][1], field[2][2], user)or\
        chek_line(field[2][0], field[1][1], field[0][2], user):
            return True
    return False