#common element between two elements
list1=[1,2,3,4,5]
list2=[2,4,5]
set1=set(list1)
set2=set(list2)
set_intersection=set1.intersection(set2)
print(list(set_intersection))

#output:
[2,4,5]