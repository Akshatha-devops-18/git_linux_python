#declare dictionary students
students = {
    "john":12,"steve":20,"robert":19, "diana":15,"riya":12
}

#find minimum value in dictionary
minimum_value = min(students.values())

#get keys with minimal value using list comprehension
minimum_keys = [key for key in students if students[key]==minimum_value]

#print the minimum keys
print(minimum_keys)



#output:
['john', 'riya']