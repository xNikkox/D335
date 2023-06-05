is_leap_year = False

input_year = int(input())


def ily(year):
    if year >= 1000 and year % 400 == 0:
        print(f"{year} - leap year")
        return True
    elif input_year % 4 == 0:
        print(f"{year} - leap year")
        return True
    else:
        print(f"{year} - not a leap year")
        return False


ily(input_year)
