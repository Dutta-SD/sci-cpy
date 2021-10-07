def fcn(x,y):
    return (x+y) #function at x+y for testing

def RK4(x0,y0,xn,n):
    h = (xn-x0)/n #calculation of the step (also called interval)
    
    for i in range(n):
        k1 = h*fcn(x0,y0)
        k2 = h*fcn((x0+h/2),(y0+k1/2))
        k3 = h*fcn((x0+h/2),(y0+k2/2))
        k4 = h*fcn((x0+h),(y0+k3))
        
        yn = y0 + (k1+2*k2+2*k3+k4)/6
        y0 = yn
        x0 = x0 + h
    
    return(xn,yn)

x_ini = float(input('Enter the value of the initial x \n'))
y_ini = float(input('Enter the value of the initial y \n'))
x_fin = float(input('Enter the value of the final x \n'))
step = int(input('Enter the value of the increments fo the x axis \n'))
  
  
print(RK4(x_ini,y_ini,x_fin,step))
