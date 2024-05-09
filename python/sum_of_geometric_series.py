#sum of geometric series
import math
a=int(input("Enter first number  of an G.P series: "))
n=int(input("Enter total number in this G.P series:"))
r=int(input("Enter Common Ratio:"))
total=(a*(1-math.pow(r,n)))/(1-r)
tn=a*(math.pow(r,n-1))
print("\n The sum of geometric progression is",total)
print("the tn term of geometric progression is",tn)

#output:
Enter first number  of an G.P series: 3
Enter total number in this G.P series:4
Enter Common Ratio:3

 The sum of geometric progression is 120.0
the tn term of geometric progression is 81.0
