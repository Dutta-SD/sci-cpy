# include <stdio.h>
# include <stdlib.h>
# include <math.h>

int main()
{
	int n,i,j,iter=1;
	float div, HighestErr, next, sum;
	printf ("Enter the number of unknowns: ");
	scanf("%d",&n);
	float AugM[n][n+1], Soln[n], tempSoln[n];
	
	for (i=0;i<n;i++) {
		Soln[i]=0.0;
		printf ("Enter the coefficients of equation %d: ", i+1);
		for (j=0;j<n;j++)
		scanf("%f",&AugM[i][j]);
		printf ("Enter solution of equation %d: ", i+1);
		scanf("%f",&AugM[i][n]);
	}
	
	//Iteration for Jacobi
	do{
		if (iter>30){
			printf("Solution does not converge in 20 iterations. Operation unsuccessful!");
			return EXIT_FAILURE;
		}
		printf("Iteration %d:\n",iter++);
		HighestErr=0.0;
		for (i=0;i<n;i++)
		{
			sum=0.0;
			for (j=0;j<n;j++){
				if (i!=j){
					sum+=AugM[i][j]*Soln[j];
				}
			}
			tempSoln[i]=(AugM[i][n]-sum)/AugM[i][i];
			if (fabs(Soln[i]-tempSoln[i])>HighestErr){
				HighestErr=fabs(Soln[i]-tempSoln[i]);	
			}
			printf("Sol[%d]=%f\n",i,tempSoln[i]);
		}
		for (i=0;i<n;i++){
			Soln[i]=tempSoln[i];	
		}
	} while (HighestErr>0.000001);
	
	//Printing solution
	printf("\nSolutions are as follows:\n");
	
	for (i=0;i<n;i++)
	printf("%c = %f\n",'z'-(n-i-1), Soln[i]);
	
	return EXIT_SUCCESS;
}
