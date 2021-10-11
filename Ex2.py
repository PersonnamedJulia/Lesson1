print ('Введите время в секундах')
time = int(input())
hours = time//360
minuts = (time - hours*360)//60 
sec = (time%360)%60
print (hours, ':', minuts, ':', sec)