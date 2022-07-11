#some_var = (2,)
#if some_var is None:

#    print("NoneType")
#else:
#    print(type(some_var))

#a = "foo"
#b = "bar"

#print(1 and a or b)

# пусть a и b - переменные, которые мы хотим проверить
#a = 0
#b = 1

#if a and b: # проверка истинности обеих переменных
#    print("Обе переменные истинные")
#    print(a,b)

#a = 0
#b = 1

#if a and b:
#    print("Обе переменные истинные")
#    print(a,b)
#elif a or b:
#    print("Одна из переменных истинная")
#    print( a or b)
#else:
#    print("Обе переменных ложные")


#a = int(input())

#if 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#    print("Истина гедто там")

#L = list(map(int, input().split()))

#print(all(L))
#скелет генератора списков
#L = [ a for a in some_iter_obj if cond ]
#L = []

#for a in some_iter_obj:
#    if cond:
#        L.append(a)
# генератор чисел

#multiplication_table = [i*10 for i in range(1,11)]
#print(multiplication_table)
# вариант по сложнее
# = [[i*j for j in range(1,11)] for i in range(1,11)]

#L = [int(input()) % 2 == 0 for i in range(5)]
# истина тогда и только тогда
# any(L) and not all(L)
# произведение двух списков
#N = [a*b for a,b in zip(L,M)]


#text = input()  # получаем строку

#last = text[0]  # сохраняем первый символ
#count = 0  # заводим счетчик
#result = ''  # и результирующую строку

#for c in text:
#    if c == last:  # если символ совпадает с сохраненным,
#        count += 1  # то увеличиваем счетчик
#    else:
#        result += last + str(count)  # иначе - записываем в результат
#        last = c  # и обновляем сохраненный символ с его счетчиком
#        count = 1

#result += last + str(count)  # и добавляем в результат последний символ
#print(result)

#def linear_solve(a, b):
#    if a: # помним, что 0 интерпретируется как False, иначе True
#        return b / a
#    elif not a and not b:  # снова используем числа в логических выражениях
#        return "Бесконечное количество корней"
#    else:
#        return "Нет корней"
#print(linear_solve(0, 0))

#def D(a, b, c):
#    return b ** 2 - 4 * a * c

#def quadratic_solve(a, b, c):
#    if D(a, b, c) < 0:
#        return "Нет вещественных корней"
#    elif D(a, b, c) == 0:
#        return -b / (2 * a)
#    else:
#        return (-b - D(a,b,c) ** 0.5) / (2 * a), (-b + D(a, b, c) ** 0.5) / (2 * a)
#миинимальный элемент списка без использование циклов и встроенной функции
#def min_list(L):
#    if len(L) == 1:
#        return L[0]
#    return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
#рекурсивную функцию, которая зеркально разворачивает число. Предполагается, что число не содержит нули.

#def mirror(a, res=0):
#    a=4566785678
#    return mirror(a // 10, res*10 + a % 10) if a else res

#def equal(N, S):
#    if S < 0:
#        return False
#    if N < 10:
#        return N == S
#    else:
#        return equal(N // 10, S - N % 10)

#last = 0
#for a in e(): # e() - генератор
#    if (a - last) < 0.00000001: # ограничение на точность
#        print(a)
#        break # после достижения которого - завершаем цикл
#    else:
#        last = a # иначе - присваиваем новое значение


#def e():
#    n = 1
#    while True:
#        yield (1 + 1 / n) ** n
#       n += 1




#iter_obj = iter("Hello!")
#print(next(iter_obj))

#yesno = input("""Введите Y, если хотите авторизоваться или N,
#             если хотите продолжить работу как анонимный пользователь: """)

#auth = yesno == "Y"


#def is_auth(func):
#    def wrapper():
#        if auth:
#            print("Пользователь авторизован")
#            func()
#        else:
#            print("Пользователь неавторизован. Функция выполнена не будет")
#    return wrapper

#USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#yesno = input("""Введите Y, если хотите авторизоваться или N,
#             если хотите продолжить работу как анонимный пользователь: """)
#auth = yesno == "Y"
#if auth:
#    username = input("Введите ваш username:")
#def from_db():
#    print("some data from database")
#    def has_access(func):
#        def wrapper():
#            if username in USERS:
#                print("Авторизован как", username)
#                func()
#            else:
#                print("Доступ пользователю", username, "запрещен")
#    return wrapper

#from_db()



# все элементы списка к нужному регистору
#L = ['THIS', 'IS', 'LOWER', 'STRING']
#print(list(map(str.lower, L)))
# Из заданного списка вывести только положительные элементы


#пример фильтра
#def positive(x):
#    return x % 2 == 0  # функция возвращает только True или False
#result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
# Возвращается итератор, т.е. перечисляйте или приводите к списку
#print(list(result))   # [1, 2]

#пример сортирокки
#data = [
#   (82, 1.91),
#   (68, 1.74),
#   (90, 1.89),
#   (73, 1.79),
#   (76, 1.84)
#]
#print(min(sorted(data, key = lambda x: x[0] / x[1] ** 2)))


# Длинна элементов списка


#a = ["asd", "bbd", "ddfa", "mcsa"]

#подсчет количтва символов в  элементе списка
#print(list(map(lambda a: len(str(a)), a)))
#print(list(map(len, a)))
#приведение к верхнему регистору всех символов элементов списка
#print(list(map(str.upper, a)))