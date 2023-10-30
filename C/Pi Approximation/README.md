# Algorithm 
1. Initialize k=1 // this variable will be used as the denominator of leibniz’s formula, it will be incremented by 2
1. Initialize sum=0 // sum will add all the elements of the series
1. Run a for loop from 0 to 1000000 //at this value, we get the most accurate value of Pi
1. Inside for loop, check if i%2==0 then do sum=sum+4/k
1. Else, do sum=sum-4/k
1. Increment k by 2, go to step 3
