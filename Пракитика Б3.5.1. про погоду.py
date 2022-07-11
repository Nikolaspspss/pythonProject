temperature = int(input("Температура?: "))
rayn = input("Есть ли дождь?: ")
hevi_rayn = input("Дождь сильный?: ")
decision = "Не решил что брать. Останусь дома."

if 30 >= temperature >= 20 and rayn == "no" :
    print("футболка и шорты")
elif 30 >= temperature >= 20 and rayn == "yes":
    print("Футболка шорты дождевик")
elif temperature < 0 :
    print("пуховик")
elif 20 > temperature > 0 and rayn == "no":
    print("пальто")
elif temperature > 0 and rayn == "yes":
    if temperature > 0 and hevi_rayn == "no":
        print("пальто и дождевик")
    if temperature > 0 and hevi_rayn == "yes":
        print("Пальто резиновые сапоги и зонт")
else:
    print(decision)




