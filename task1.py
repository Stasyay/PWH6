# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
#     [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

lst = [2, 100, 2, -9, 98]
summa = 0

for i in range(len(lst)):
    if i%2 !=0:
        summa += lst[i] 

print (lst)
print (f'сумма чисел на нечетных индексах =  {summa}')

##################################
# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

print(f'решено при помощи функции  list comprehension =  {sum([lst[i] for i in range(len(lst)) if i%2 != 0])}')