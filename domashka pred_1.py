# Вычислить число Пи c заданной точностью d
# Пример:
#
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
import math     # Импорт ставить в начале кода и после него две пустые строки - правило


# d = int(input('Введите точность(кол-во знаков после запятой) числа Пи '))

print(round(math.pi, int(input('Введите точность(кол-во знаков после запятой) числа Пи '))))


# Второй вариант, если задавать точность как прописано в условии
import math


d = input('Задайте точность числа пи: ')
d1 = len(d) - 2
if 1 <= d1 <= 10:
    print(round(math.pi, d1))
else:
    print('Не правильное значение d')


# Третий вариант - с функциями
import math

# Функция
def Accuracy(data):
    i = 0
    while(1 > data):
        i += 1
        data = data * 10
    return i

def AccuracyPI(precision):
    return round(math.pi, precision)

precision = float(input('Input precision (example: 0.001): '))
print(f'{AccuracyPI(Accuracy(precision))}')