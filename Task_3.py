# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


print ('Это программа, которая выведет список неповторяющихся элементов исходной последовательности')
num = input('Введите число для проверки: ')
result = []
count = 0 
for i in range (len(num)):
    for j in range (len(num)):
        if num[j] == num [i] :
            count += 1
    if count == 1:
        result.append(num[i])
    count = 0
    
print (result)
