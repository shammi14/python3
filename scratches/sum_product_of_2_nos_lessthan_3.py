#Write a program to read 2 integers and chk if sum and product of two numbers less than 3.
# Result should be a Boolean value.
A = int(input())
B = int(input())
total = A + B
product = A * B
count = 0

while total > 0 or product > 0:
    total = total // 10
    product = product // 10
    count += 1

if count < 3:
    print(True)
else:
    print(False)