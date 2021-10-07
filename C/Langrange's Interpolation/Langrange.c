# include <stdio.h>
# include <stdlib.h>

int main ()
{
	int n,i,j;
	printf("**** Langrange's Method of Interpolation**** \n\n\n");
	printf ("Enter the number of observations: ");
	scanf("%d",&n);
	float x[n],f[n],result=0.0,temp,X;
	for (i=0;i<n;i++){
		printf("Enter x%d & f%d : ",i+1,i+1);
		scanf("%f %f",&x[i],&f[i]);
	}
	
	//Enter the value of X the result of which we want to find out
	printf ("Enter x for finding f(x): ");
	scanf("%f",&X);
	
	//Calculation of Langrange
	for (i=0;i<n;i++){
		temp=1.0;
		for (j=0;j<n;j++){
			if (j!=i){
				temp*=(X-x[j])/(x[i]-x[j]);
			}
		}
		result+=temp*f[i];
	}
	
	printf("f(%f) = %f",X,result);
	return EXIT_SUCCESS;
}
