#Ray Tso
#1/22/18
#slope.py



x1= float(input('enter the slope of x1='))
y1= float(input('enter the slope of y1='))
x2= float(input('enter the slope of x2='))
y2= float(input('enter the slope of y2='))
m=(y2-y1)/(x2-x1)
b=(y1-m*x1)
print(' The slope is', m)
print(' The equation of the line is Y=',m,'x','+',b)
