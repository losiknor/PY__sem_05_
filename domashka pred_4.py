# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 1 до 100,
# можно создать свой генератор случайных чисел или использовать готовый)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# k=2 => 2*x² + 4*x + 5 = 0
import random

# from useFulFutires.IsNumber import isNumber

k = 5# isNumber()
count = k
randomKoef = [random.randint(0, 100) for i in range(k+1)]

resultT = ""
for i in range(k):
    if i == k-1:
        resultT += str(randomKoef[i]) + '*x + '
        resultT += str(randomKoef[i+1])
        break
    else:
        resultT += str(randomKoef[i]) + f'*x**{count} + '
    count -= 1

resultT += ' = 0'
print(resultT)
path = 'randomCoefPolynom.txt'

with open(path, 'w') as d:
    d.write(resultT)

# Второй вариант
k = int(input('Введите степень k: '))

import random
mass = random.sample(range(9), k+1)

print(mass)

file = open('Task4.txt', 'w')
p = k
for i in range(len(mass)-1):
    file.write(f'{mass[i]}x^{p} + ')
    p = p - 1
file.write(f' {mass[k]} = 0' + '\n')
file.close()