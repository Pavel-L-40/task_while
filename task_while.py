# Задача "Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count = i = 0
while count < len(my_list) and i >= 0:
    i = my_list[count]
    if i > 0:
        print(i)
    count = count + 1