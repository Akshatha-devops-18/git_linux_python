import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])
del number[2]  # removing third element
print(number)  # Output: array('i', [1, 2, 3, 4])



#output:
array('i', [1, 2, 3, 4])