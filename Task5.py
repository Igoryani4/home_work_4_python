list1 = '23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + x^2 + 20 = 0'
list2 = '17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x + 33 = 0'

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
                list_k1[b]=(list1_2[i][:j-1])
    else:
        b = 0
        list_k1[b] = (list1_2[i])
        
for i in range (len(list2_2)):
    if 'x' in list2_2[i]:
        for j in range(len(list2_2[i])):
            if list2_2[i][j] == '^':
                b =int(list2_2[i][j+1])
                list_k2[b]=(list2_2[i][:j-1])
    else:
        b = 0
        list_k2[b] = (list2_2[i])
