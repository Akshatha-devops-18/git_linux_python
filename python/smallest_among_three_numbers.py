# Python program to find the smallest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

if (num1 <= num2) and (num1 <= num3):
   smallest= num1
elif (num2 <= num1) and (num2 <= num3):
   smallest = num2
else:
   smallest = num3

print("The smallest number is", smallest)

#output:
The smallest number is 10