def determine_season(month, day):
    # Dictionary to hold each month and its maximum day.
    days_in_month = {
        "January": 31,
        "February": 29,  # accounting for leap years
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    # check if month is valid
    if month not in days_in_month:
        return "Invalid"

    # check if day is valid for given month
    if day < 1 or day > days_in_month[month]:
        return "Invalid"

    # define season based on month and day
    if (month == "March" and day >= 20) or (month == "April") or (month == "May") or (month == "June" and day <= 20):
        return "Spring"
    elif (month == "June" and day >= 21) or (month == "July") or (month == "August") or (month == "September" and day <= 21):
        return "Summer"
    elif (month == "September" and day >= 22) or (month == "October") or (month == "November") or (month == "December" and day <= 20):
        return "Autumn"
    else:
        return "Winter"


# input from user
month = input()
day = int(input())

# determine and print season
print(determine_season(month, day))
