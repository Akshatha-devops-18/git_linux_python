#to print pattern
 #     *
 #    * *
 #   * * *
 #  * * * *
 # * * * * *

n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()

#output:
Enter the number of rows:5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 