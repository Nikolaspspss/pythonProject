array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i in range(len(array)): # проходим по всему массиву

        idx_min = i # сохраняем индекс предположительно минимального элемента

        for j in range(i+1, len(array)):
                if array[j] < array[idx_min]:
                        idx_min = j
                count += 1
        if i != idx_min:# если индекс не совпадает с минимальным, меняем
                array[i], array[idx_min] = array[idx_min], array[i]

        idx_max = i
        
        for j in range(i, len(array)):
            if array[j] > array[idx_max]:
                idx_max = j
        if i != idx_max:
            array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(count)


