# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list
print(list(itertools.permutations([1, 2, 3])))


#output:
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]