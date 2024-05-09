def f():
    s = "I love Geeksforgeeks"
    print(s)
# Driver code
f()
# This function uses global variable s
def f():
    print("Inside Function", s)
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

#output:
I love Geeksforgeeks
Inside Function I love Geeksforgeeks
Outside Function I love Geeksforgeeks
