string=input("Enter the string in camel case:")
string=string[0].lower() + string[1:] #xtraCoding
for i in string:
    if i.isupper():
        string=string.replace(i,f"_{i.lower()}")
print(string)


#output:
Enter the string in camel case:Hi Akshatha
hi_akshatha


