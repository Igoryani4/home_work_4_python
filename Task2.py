#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math
print ('Это программа, которая которая составит список простых множителей числа N')
num = int (input('Введите число: '))
num_2 = num
i = 2
count = 0
flag = False
div = []
while num_2 != 1:
    for k in range(1, i+1):
        if i % k == 0:
            count += 1 
    if count == 2:
        flag = True
        count = 0   
        
    if num_2 % i == 0 and flag == True:
        num_2 /= i 
        div.append(str(i))
        flag = False
    else:
        i += 1
print(f'Простые делители для числа {num} =','*'.join(div))
