#include<stdio.h>

float fun(float x, float y)
{
    return	(x+(y*y)); // dy/dx = (x + y*y) 
}
 
float rungeKutta(float x0, float y0, float xn, float h)
{
    int n = (int)((xn - x0) / h);
 
    float k1, k2, k3, k4, k5, y = y0;
 
    for(int itr=1; itr<=n; itr++)
    {
        // Runge Kutta Formulas to find next value of y
         
        k1 = h*fun(x0, y);
        k2 = h*fun(x0 + (h/2), y + (k1/2));
        k3 = h*fun(x0 + (h/2), y + (k2/2));
        k4 = h*fun(x0 + h, y + k3);
 
        y +=  ((k1 + 2*k2 + 2*k3 + k4)/6.0);
 
        x0 +=  h;

    }
 
    return y;
}
 
//main function
int main()
{
    float x0, y, xn, h;
    
    printf("Enter the value of initial x: ");
    scanf("%f",&x0);
    printf("Enter the value of initial y: ");
    scanf("%f",&y);
    printf("Enter the value of final x: ");
    scanf("%f",&xn);
    printf("Enter the value of the increments fo the x axis: ");
    scanf("%f",&h);
     
    printf("\nThe value of y at x is : %f", rungeKutta(x0, y, xn, h));
    return 0;
}
