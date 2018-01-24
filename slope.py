#Ray Tso
#1/22/18
#slope.py



x1= float(input('enter the slope of x1='))
y1= float(input('enter the slope of y1='))
x2= float(input('enter the slope of x2='))
y2= float(input('enter the slope of y2='))
slope=(y2-y1)/(x2-x1)
equ_of_line=(slope*x1-y1)
print(' The slope is', slope)
print(' The equation of the line is Y=',slope,'x','+',equ_of_line)
