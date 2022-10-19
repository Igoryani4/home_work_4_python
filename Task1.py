
#Вычислить число Пи c заданной точностью d
#Пример:
#при d = 0.001, π = 3.141
#при d = 0.1, π = 3.1
#при d = 0.00001, π = 3.14154
#d от 0.1 до 0.0000000001

#!!! не округлять константу math
import math

print('Вы хотите ввести диапазон чисел или одно число? :')
value = int (input('Введите "1" если хотите ввести одно число и "0" если диапазон: '))
pi = str(math.pi)
if value == 1:
    print('Задайте точность вычисления Пи: ')

    accuracy_pi = input('Введите параметр: ')
    
    print (pi[:len(accuracy_pi)])
    
else :
    range_pi_1 = input ('Введите начало диапазона: ')
    range_pi_2 = input ('Введите конечный параметр диапазона:')
    len_rang_1 = len(range_pi_1)
    len_rang_2 = len(range_pi_2)
    for i in range (len_rang_2):
        print(pi[:len_rang_1+i])
