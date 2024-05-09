#frequency of each char in string
#Python3 code to demonstrate
# each occurrence frequency using
# collections.Counter()
from collections import Counter
# initializing string
test_str = "GeeksforGeeks"
# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)
# printing result
print("Count of all characters in GeeksforGeeks is :\n " + str(res))


#output:
Count of all characters in GeeksforGeeks is :
Counter({'e': 4, 'G': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})
