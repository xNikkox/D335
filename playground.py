is_leap_year = False

input_year = int(input())

''' Type your code here. '''
if input_year >= 1000 and input_year % 400 == 0:
    print(f"{input_year} - leap year")
    is_leap_year == True
elif input_year % 4 == 0:
    print(f"{input_year} - leap year")
    is_leap_year == True
else:
    print(f"{input_year} - not leap year")
