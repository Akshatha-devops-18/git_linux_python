#to print pattern
#*
#* *
#* * *
#* * * *
#* * * * *

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

#output:
Enter number of rows: 5
* 
* * 
* * * 
* * * * 
* * * * * 