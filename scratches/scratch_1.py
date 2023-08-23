#
a=int(input())
b=int(input())
c=int(input())
total_of_1st_two_numbers =a+b
total_of_last_two_numbers= b+c
total_of_1st_and_last_numbers= c+a
if total_of_1st_two_numbers>10 and total_of_last_two_numbers>10 and total_of_1st_and_last_numbers>10:
    print(True)
else:
    print(False)