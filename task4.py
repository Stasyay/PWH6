# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
#     пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
mult = 1

for el in range(1,n+1):
    mult *= el
    print(f"{mult}", end = " ")
print('')


##################################
# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * f(x -1)
lst = [f(i) for i in range(1, n +1)]
print(lst)


# factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
# print(factorial(4))

