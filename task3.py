#     Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 0, 10.01]
new_lst = []

for el in range(len(lst)):
    new_lst.append(lst[el]%1)
print(max(new_lst) - min(new_lst))

##################################
# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


print(max(lst[el]%1 for el in range(len(lst))) - min(lst[el]%1 for el in range(len(lst))))