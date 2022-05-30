# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов (нет нулевых кофициентов).
# from sympy import parse_expr, symbols
#
# path1 = 'Polynom1.txt'
# path2 = 'Polynom2.txt'
# with open(path1, 'r') as file:
#     mNumber = file.read()
# with open(path2, 'r') as file:
#     mNumber2 = file.read()
# print(f'({mNumber}) + ({mNumber2})')
# x = symbols('x')
# mNumber = parse_expr(mNumber.replace('^', '**'), local_dict={'x': x})
# mNumber2 = parse_expr(mNumber2.replace('^', '**'), local_dict={'x': x})
# sumMNumbers = mNumber + mNumber2
# print(f'({mNumber}) + ({mNumber2})')
# print(f'{mNumber} + {mNumber2}')
# print(sumMNumbers)

str_1 = "1x^7 + 6x^6 + 3x^5 + 7x^4 + 8x^3 + 2x^2 + 5x^1 + 0".split(' ')
str_2 = "3x^7 + 65x^6 + 7x^5 + 9x^4 + 33x^3 - 18x^2 + 2x^1 + 13".split(' ')
print(str_1)
print(str_2)
print(str_1[0].split('x'))

