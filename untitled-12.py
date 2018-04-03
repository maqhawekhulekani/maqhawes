r = int ( input ("enter the radius of the circle "))
circle_x = int ( input ("enter x cord of the centre "))
circle_y = int ( input ("enter y cord of the centre "))
point_x = int ( input ("enter x cord of the point "))
point_y = int (input ("enter y cord of the point "))
d = ((circle_x**2 - point_x**2)+(circle_y**2 - point_y**2))
if d <= r :
    area = (r+r)**2
    print ("area = " , area)
else :
    print ("outside of the circle")