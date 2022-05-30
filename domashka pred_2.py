# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
import math
n = int(input('Задайте натуральное число N: '))
n1 = n
numbers = []
for i in range (2, int(math.sqrt(n))+1):
    while (n1 % i == 0):
        numbers.append(i)
        n1 //= i
if (n1 != 1):
    numbers.append(n1)
print(f'Простые множители числа {n}: ', numbers)

# Второй вариант
n = int(input())
lst = []
for i in range(2,int(n**0.5)+1):
    while n%i == 0:
        lst.append(i)
        n /= i
    if n == 1:
        break
print(lst)