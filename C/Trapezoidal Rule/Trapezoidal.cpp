# include <stdio.h>
# include <stdlib.h>
#include<math.h>

#define f(x) 1/(1+pow(x,2))//change it depending on the input function

int main ()
{
	float a,b,n,h,area,sum=0;
	int i;
	printf("**** Trapezoidal Method of Numerical Integration **** \n\n\n");
	printf("Enter the lower limit:a= ");
	scanf("%f",&a);
	printf("\nEnter the upper limit:b= ");
	scanf("%f",&b);
	printf("\nEnter the number of division:");
	scanf("%f",&n);
	h=(b-a)/n;
	
	//Computation for Trapezoidal rule
	sum=(f(a)+f(b))/2;
	for(i=1;i<n;i++){
		sum=sum+f(a+h*i);
	}
	area=h*sum;
	printf("\n\nThe area under the curve within the limit is : %f",area);
	return 0;
}
