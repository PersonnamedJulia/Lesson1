print ('Введите выручку фирмы')
proceeds = int(input())
print ('Введите издержки фирмы')
costs = int(input())
if proceeds > costs:
    print ('финансовый результат фирмы - прибыль')
    print ('рентабельность фирмы', float((proceeds - costs)/proceeds))
    print ('введите количество сотрудников фирмы')
    persons = int(input())
    print('прибыль фирмы на одного сотрудника', float ((proceeds - costs)/persons))
else: 
    print ('финансовый результат фирмы - убыток')