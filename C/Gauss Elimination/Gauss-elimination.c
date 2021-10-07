# include <stdio.h>
# include <stdlib.h>

int main ()
{
	int n,i,j,k,temp;
	float div;
	printf ("Enter the number of unknowns: ");
	scanf("%d",&n);
	float Soln[n], sum;
	float **AugM=(float**)malloc((n)*sizeof(float*));
	for (i=0;i<n;i++) {
		AugM[i]=(float*)malloc((n+1)*sizeof(float));
		printf ("Enter the coefficients of equation %d: ", i+1);
		for (j=0;j<n;j++){
			scanf("%f",&AugM[i][j]);
		}
		printf ("Enter solution of equation %d: ", i+1);
		scanf("%f",&AugM[i][n]);
	}
	
	//Displaying the Equations
	printf("Equations are:\n\n");
	for (i=0;i<n;i++){
		for (j=0;j<n-1;j++){
			printf("%f%c + ", AugM[i][j],'z'-(n-j-1));
		}
		
		printf("%f%c = %f\n", AugM[i][j],'z'-(n-j-1), AugM[i][n]);
	}
	
	//Elimination
	for (k=0;k<n-1;k++){
		if (AugM[k][k]==0.0){
			for (i=k+1;i<n;i++){
				if (AugM[i][k]!=0.0){
					for (j=k;j<n+1;j++){
						temp=AugM[k][j];
						AugM[k][j]=AugM[i][j];
						AugM[i][j]=temp;
					}
				break;
				}
			}
		} // To get non-zero diagonal
		for (i=k+1;i<n;i++){
			div=AugM[i][k]/AugM[k][k];
			for (j=k;j<n+1;j++){
				AugM[i][j]-=div*AugM[k][j];
			}
		}
	}
	
	//Checking existence of solution
	for (i=0;i<n;i++){
		if (AugM[i][i]==0.0){
		printf("No unique solution!\n");
		
		return EXIT_FAILURE;
		}
	}
	
	//Back substitution
	Soln[n-1]=AugM[n-1][n]/AugM[n-1][n-1];
	for (i=n-2;i>=0;i--){
		sum=0.0;
		for (j=i+1;j<n;j++){
			sum+=AugM[i][j]*Soln[j];
		}
		Soln[i]=(AugM[i][n]-sum)/AugM[i][i];
	}
	
	//Printing solution
	printf("\nSolutions are as follows:\n");
	for (i=0;i<n;i++){
		printf("%c = %f\n",'z'-(n-i-1),Soln[i]);
	}
	
	
	return EXIT_SUCCESS;
}
