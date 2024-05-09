#largest word in string
str=input("enter string")
s=str.split()
max=0
for ele in s:
    if len(ele)>max:
        max=len(ele)
        max_word=ele
print("word with maximum length in given string is:",max_word)
print("Maximum length is:",len(max_word))


#output:
enter string:find the largest word
word with maximum length in given string is: largest
Maximum length is: 7
