print ('введите целое положительное число')
number = int(input())
max = number%10
while number//10 != 0:
  number = number//10
  if max < number%10: max = number%10
print (n)