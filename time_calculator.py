def add_time(start, duration, day=None):

    # splitting up the start time and duration
    hour_start = int(start.split(":")[0])
    minute_start = int(start.split(":")[1][0:2])
    period = start.split(" ")[1]

    hour_duration = int(duration.split(":")[0])
    minute_duration = int(duration.split(":")[1])

    days_list = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

    # converting to 24 hour clock to start with
    if period == "PM":
        hour_start += 12

    new_hour = hour_start + hour_duration
    new_minute = minute_start + minute_duration

    # increasing hour by 1 if new_minute is one hour or more
    if int(new_minute) > 59:
        new_hour += 1
        new_minute -= 60

    # setting a counter for number of days passed and resetting hour
    days_passed = 0
    while new_hour > 23:
        new_hour -= 24
        days_passed += 1

    # changing period
    if new_hour > 12 and (new_hour % 12) != 0:
        period = "PM"
    else:
        period = "AM"

    new_hour = new_hour % 12

    if new_hour % 12 == 0 and period == "AM":
        period = "PM"

    # changing new_hour from 0 to 12
    if new_hour % 12 == 0 and period == "AM":
        period = "PM"

    if new_hour == 0 and period == "AM":
        new_hour = 12
    elif new_hour == 0 and period == "PM":
        new_hour = 12

    # adding 0 in front of the minute digit if new_minute < 10, i.e. of length 1
    if len(str(new_minute)) == 1:
        new_minute = "0" + str(new_minute)

    # getting output in required format
    new_time = str(new_hour) + ":" + str(new_minute) + " " + period

    if day:
        new_day = days_list[(days_list.index(day.upper()) + days_passed) % 7].capitalize()
        new_time += f", {new_day}"

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"


    return new_time

print(add_time("11:40 AM", "0:25", "Monday"))