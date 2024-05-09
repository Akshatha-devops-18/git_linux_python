## initializing the string and the word
string = "I am programmer. I am student."
word = "am"
## splitting the string at space
words = string.split()
## initializing count variable to 0
count = 0
## iterating over the list
for w in words:
    if w == word:
        count += 1
 ## printing the count
print(count)


#output:
2