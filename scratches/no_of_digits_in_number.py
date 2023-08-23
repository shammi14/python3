#write a program to count the number of digits in a number.
n=int(input("Enter number:"))
m = int(input("Enter number:"))
count=0
while(n>0 and m > 0):

    n=n//10
    m = m//10
    count = count + 1
print("The number of digits in the number are:",count)