#include<stdio.h>
#include<math.h>
#include<process.h>
#include<stdlib.h>

//EPSILON is a very small quantity representing the maximun allowed error
#define EPSILON 0.000001

//Equation to be solved is f(x)=0
//Modify the equation to be solved by changing f(x) and f1(x)
//f(x) returns the value of f(x) at a given value of x
float f(float x)
{
	return(x*x-25);//This is the function f(x), make modifications here
}


//Equation to be solved is f(x)=0
//Modify the equation to be solved by changing f(x) and f1(x)
//f1(x) returns the value of first order derivative of f(x) with respect to the variable x at a given value of x
float f1(float x)
{
	return 2*x;//This is the derivative of the function f(x), make modifications here
}	



//Returns the root of the equation f(x)=0, if it can be calculated. Otherwise exits the program.
float NewtonRaphson(float x0)
{
	while(f(x0)>EPSILON || f(x0)<(-EPSILON))
	{
		if(f1(x0)==0)
		{
			printf("Derivative becomes 0 at %f",x0);
			exit(0);
		}
		x0=x0-(f(x0)/f1(x0));
	}
	return x0;
}



//Driver code to test the above functions
int main()
{
	float x0;//Guess for the solution

    printf("\n\t***SOLUTION OF EQUATIONS BY NEWTON RAPHSON METHOD***");

    printf("\n\nINSTRUCTIONS:\nEquation to be solved is denoted by f(x)=0\nThe first order derivative of f(x) with respect to the variable x is denoted by f1(x)\nThe equation to be solved can be modified by changing the following functions in the source code : f(x) and f1(x)\n\nInput : A guess for the solution\nOutput : A solution for the equation if possible. If a solution can not be calculated, the program exits.");

    printf("\n\nPlease enter a guess for the solution : ");
	scanf("%f",&x0);

	printf("A root of the equation is : %f",NewtonRaphson(x0));
	return 0;
}