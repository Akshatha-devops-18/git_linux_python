#print even numbers
#in range

ll=int(input("Enter lower limit "))
ul=int(input("Enter upper limit "))

print("Even numbers in the range are")

# loop

for i in range(ll,ul):
    if i%2==0:
        print(i,end=" ")


#output:
Enter lower limit 2
Enter upper limit 8
Even numbers in the range are
2 4 6 