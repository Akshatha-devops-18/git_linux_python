#GCD of two numbers
import math

# prints 12

print("The gcd of 60 and 48 is : ", end="")

print(math.gcd(60, 48))

#or

def hcf(a,b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)



a = 60

b = 48


# prints 12

print("The gcd of 60 and 48 is : ", end="")

print(hcf(60, 48))

#output:
The gcd of 60 and 48 is 12