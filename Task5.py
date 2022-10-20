list1 = '23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + x^2 + 20 = 0'
list2 = '17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x + 33 = 0'

list1_1 = list1.replace(' ', '')[: -2]
list2_1 = list2.replace(' ', '')[: -2]

list1_2 = list1_1.replace('-', '+-').split('+')
list2_2 = list1_1.replace('-', '+-').split('+')
