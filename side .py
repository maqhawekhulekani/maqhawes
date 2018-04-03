num1 = int ( input ("enter your first number :"))
num2 = int ( input ("enter your second number :"))
num3 = int ( input ("enter your third number :"))
if num1 < num2 and num1 < num3 :
   if  num2 % num1 == 0 and num3 % num1 == 0:
      print (num1)
elif num2 < num1 and num2 < num3 :
   if  num3 % num2 == 0 and num3 % num2 == 0 :
      print (num2)

elif num3 < num1 and num3< num2 :   
   if  num1 % num3 == 0 and num2 % num3 == 0:
      print (num3)
elif num1==num2 and num1 == num3:
   print(num1)

if num1 < num2 and num1 < num3 :
   for num in range(1,num1):
      if num2 % num == 0 and num3 % num == 0 and num1 % num == 0 and num :
         print (num)

if num2 < num3 and num2 < num3 :
    for num in range(1,num2):
      if num2 % num == 0 and num3 % num == 0 and num1 % num == 0 :
         print (num)
if num3 < num1 and num3 < num2 :
   for num in range(1,num3):
      if num2 % num == 0 and num3 % num == 0 and num1 % num == 0 :
         print (num)