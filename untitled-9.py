
s = float (input ("starting time as a float 2 decimal place "))
f = float (input ("finishing time as a float 2 decimal place "))
hours = f- s
if s >= 18.00 and f <= 21.30 :
    price = 25*hours  
    print ("price = R",price)
elif s >= 21.30 and f <= 24.00:
    price = 35*hours
    print("price = R",price)
else :
    print ("invalid time")