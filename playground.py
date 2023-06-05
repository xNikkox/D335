is_leap_year = False

input_year = int(input())


def ily(year):
    if year % 400 == 0:
        print(f"{year} - leap year")
        return True
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} - leap year")
        return True
    else:
        print(f"{year} - not a leap year")
        return False


ily(input_year)
