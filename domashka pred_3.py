# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

# Неправильное решение
# numbers = [3, 5, 3, 8, 8, 2, 5]
# print ('Исходная последовательность чисел')
# print (numbers)
# # print (f'Исходная последовательность чисел:\n{numbers}') --->  то же что строки 4-5
# new_numbers = []
# for i in numbers:
#     if i not in new_numbers:
#         new_numbers.append(i)
# print ('Последовательность неповторяющихся элементов')
# print (new_numbers)

# Правильное решение:
mass = [int(i) for i in input('Введите числа массива через пробел ').split()]
print(mass)

def unique_mass_num(mass):
    unique = []

    for i in mass:
        if mass.count(i) == 1:

            unique.append(i)
    return unique

print(unique_mass_num(mass))

# Бонус - СРЕЗ
import math
n = 3
print(sr(math.pi)[:n+2])