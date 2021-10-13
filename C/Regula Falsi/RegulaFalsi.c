#include<stdio.h>
#include<math.h>
#include<process.h>
#include<stdlib.h>

//EPSILON is a very small quantity representing the maximun allowed error
#define EPSILON 0.000001

//Equation to be solved is f(x)=0
//Modify the equation to be solved by changing f(x)
//f(x) returns the value of f(x) at a given value of x
float f(float x)
{
	return(x*x-25);//This is the function f(x), make modifications here
}
	

//Returns the root of the equation f(x)=0, if it can be calculated. Otherwise exits the program.
float RegulaFalsi(float x1,float x2)
{
	float x0;
	if(f(x1)*f(x2)>0)
	{
		printf("Invalid choice of interval!");
		exit(0);
	}
	else if(f(x1)*f(x2)==0)
	{
		if(f(x1)==0)
			return x1;
		if(f(x2)==0)
			return x2;
	}		
	while(1)
	{
		x0=(x1*f(x2)-x2*f(x1))/(f(x2)-f(x1));
		if(f(x0)<=EPSILON && f(x0)>=(-EPSILON))
			return x0;
		if(f(x1)*f(x0)<0)
			x2=x0;
		if(f(x2)*f(x0)<0)
			x1=x0;
	}
}


//Driver code to test the above functions
int main()
{
    float x1,x2;//Boundaries of the closed interval such that the values of f(x) at the boundary points are opposite in sign

    printf("\n\t***SOLUTION OF EQUATIONS BY REGULA FALSI METHOD***");

    printf("\n\nINSTRUCTIONS:\nEquation to be solved is denoted by f(x)=0\nThe equation to be solved can be modified by changing the following function in the source code : f(x) \n\nInput : The left and right boundaries of a closed interval such that the values of f(x) at the boundary points are opposite in sign\nOutput : A solution for the equation if possible. If a solution can not be calculated, the program exits.");

    
    printf("\n\nEnter the left and right boundaries in order of the closed interval as mentioned above:");
	scanf("%f%f",&x1,&x2);

	printf("%f",RegulaFalsi(x1,x2));
	return 0;
}
