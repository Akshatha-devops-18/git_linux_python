#to print pattern
#A
#B C
#D E F
#G H I J
#K L M N 0
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(0,rows):
    for j in range(0,i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

        ascii_value += 1
    print()

#output:
Enter number of rows: 5
A 
B C 
D E F 
G H I J 
K L M N O 
