#sum of all elements in a list
#Python program to find sum of elements in list



total = 0



# creating a list

list1 = [11, 5, 17, 18, 23]



# Iterate each element in list

# and add them in variable total

for ele in range(0, len(list1)):
    total = total + list1[ele]



# printing total value

print("Sum of all elements in given list: ", total)

#or
list1 = [11, 5, 17, 18, 23]



# using sum() function

total = sum(list1)



# printing total value

print("Sum of all elements in given list: ", total)


#output:
Sum of all elements in given list:  74
Sum of all elements in given list:  74
