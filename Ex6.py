print('Введите результат первого дня')
a = float(input())
print ('Введите желаемый результат')
b = int (input())
day = 1
while a < b :
    day = day + 1
    a = a + a*0.1
print ('на', day, 'день пробежки спортсмен достиг результата - не менее', b, 'км')