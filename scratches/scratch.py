#Write a program that reads a 3 digit number and checks if a zero is present in it
number=input()
first_digit=number[0]
second_digit=number[1]
third_digit=number[2]
first_number=int(first_digit)
second_number=int(second_digit)
third_number=int(third_digit)
if first_number==0 or second_number==0 or third_number==0:
    print(True)
else:
    print(False)