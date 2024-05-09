#sum of square of numbers from 1 to n
n=int(input("Enter number upto which you want to sum:"))
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print("Sum=",sum)

#output:
Enter number upto which you want to sum:3
Sum= 14