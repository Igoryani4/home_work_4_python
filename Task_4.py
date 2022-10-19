# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random


k = int (input('Введите k - максимальную степень многочлена: '))
len_list = k + 1 

polynomial = []
for i in range (len_list):
    polynomial.append(str(random.randint(-100,100)))
var = 0
for i in range (len_list):
    if polynomial[i] == '0':
        continue
    elif i == k - 1:
        var = (f'{polynomial[i]}x')
        polynomial[i] = var
    elif i == k:
        var = (f'{polynomial[i]}')
        polynomial[i] = var
    else:

        var = (f'{polynomial[i]}x{k-i}')
        polynomial[i] = var
  
print (polynomial)
result = 0
for i in range (len(polynomial)):
    if polynomial[i] == '0':
        continue
    elif '-' in polynomial[i] :
        print(polynomial[i], end = '')
    else:
        print(f'+{polynomial[i]}', end = '')
print(' = 0 ')
