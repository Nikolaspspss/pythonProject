#L = ['a', 'b', 'c']
#print(id(L))

#L.append('d')
#print(id(L))


#a = 5
#b = 3+2

#print(id(a)-id(b))

#a = 0
#b = 0

#while id(a) == id(b):
#    a -= 1
#    b -= 1

#print(a)

#shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
#list_id_before = id(shopping_center[-1])

#shopping_center[-1].append("Uniqlo")
#list_id_after = id(shopping_center[-1])
#print(list_id_before == list_id_after)
#text = input("Введите текст:")

#unique = set(text)

#print("Количество уникальных символов: ", len(unique))
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.symmetric_difference(b_set)

print(a_and_b)