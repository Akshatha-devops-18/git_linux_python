#frequency of each element
# Import the 'collections' module, which provides specialized container data types
import collections

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Use the 'collections.Counter' function to count the frequency of each element in 'my_list' and store it in 'ctr'
ctr = collections.Counter(my_list)

# Print the frequency of the elements in the list, as provided by the 'ctr' object
print("Frequency of the elements in the List : ", ctr)

#output:
Original List :  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
Frequency of the elements in the List :  Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
