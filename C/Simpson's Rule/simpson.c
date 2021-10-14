#include<stdio.h>
#include<math.h>

//Function we want to integrate 
double f(double x){
  double z=x+2; // we will change the operation we want here
  return z;
}
 
void main(){
  int s;
  double a,b,y,x,sum=0,integral;
  printf("Enter the no. of even sub-intervals: ");
  scanf("%d",&s);
  printf("\nEnter the initial limit: ");
  scanf("%lf",&a);
  printf("\nEnter the final limit: ");
  scanf("%lf",&b);
  y=fabs(b-a)/s;
  /* This 'for' loop is used to divide the graph in the number of slabs as specified by the user */
  for(int i=1;i<s;i++){
    x=a+i*y;
    if(i%2==0){
      sum=sum+2*f(x);
    }
    else{
      sum=sum+4*f(x);
    }
  }
  integral=(y/3)*(f(a)+f(b)+sum);
  printf("\nThe integral of the function is: %lf\n",integral);
}
