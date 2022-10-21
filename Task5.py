with open('t1.txt', 'w') as f:
    f.write('23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + x^2 + 20 = 0')
   
with open('t2.txt', 'w') as d:
   d.write('17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x + 33 = 0')

with open('t1.txt', 'r') as f:
   list1= f.readline()
   
with open('t2.txt', 'r') as f:
   list2= f.readline()

list1_1 = list1.replace(' ', '')[: -2]
list2_1 = list2.replace(' ', '')[: -2]

list1_2 = list1_1.replace('-', '+-').split('+')
list2_2 = list2_1.replace('-', '+-').split('+')


list_k1= [ 0 for x in range (int(list1_2[0][-1])+1)]
list_k2 = [ 0 for x in range (int(list2_2[0][-1])+1)]


for i in range (len(list1_2)):
    if 'x' in list1_2[i]:
        for j in range(len(list1_2[i])):
            if list1_2[i][j] == '^':
                b =int(list1_2[i][j+1])
                if len(list1_2[i]) == 3:
                    list_k1[b] = '1'
                    continue
                
                list_k1[b]=(list1_2[i][:j-1])
    else:
        b = 0
        list_k1[b] = (list1_2[i])
        
for i in range (len(list2_2)):
    if 'x' in list2_2[i]:
        for j in range(len(list2_2[i])):
            if list2_2[i][j] == '^':
                b =int(list2_2[i][j+1])
                if len(list2_2[i]) == 3:
                    list_k1[b] = '1'
                    continue
                
                list_k2[b]=(list2_2[i][:j-1])
    else:
        b = 0
        list_k2[b] = (list2_2[i])
result =[]       
for i in range (len(list_k1)):
    result.append(int(list_k1[i]) + int(list_k2[i]))
i = len(result) - 1 

while i >= 0:
    if result[i] == 0:
        i -= 1
        continue
    elif i == 0:
        print(f'+{result[i]}', end = '')
    elif result[i] < 0 :
        print(f'{result[i]}x^{i}', end = '')
    elif i == len(result)-1 :
        print(f'{result[i]}x^{i}', end = '')
    else:
        print(f'+{result[i]}x^{i}', end = '')
    i -= 1
print(' = 0 ')
