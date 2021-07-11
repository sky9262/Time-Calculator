

def add_time(start,duration,day=None):
    time,period = start.split()
    day_later = 0
    hr_start,min_start = time.split(":")
    hr_duration,min_duration = duration.split(":")

    DAYS_OF_WEEK = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
    ]

    hr_start = int(hr_start)
    min_start = int(min_start)
    hr_duration = int(hr_duration)
    min_duration = int(min_duration)

    while min_duration > 59:
        min_duration -= 60
        hr_duration += 1

    result_hr = hr_start + hr_duration
    result_min = min_start + min_duration

    while result_min > 59:
        result_hr +=1
        result_min -= 60

    while result_hr > 12:
        result_hr -= 12
        if period == "PM":
            period = "AM"
            day_later +=1
        elif period == "AM":
            period = "PM"
        

    if hr_start < 12 and  result_hr == 12:
        if period == "PM":
            period = "AM"
            day_later +=1
        elif period == "AM":
            period = "PM"

    count_day = ""
    if day_later == 1:
        count_day = "(next day)"
    elif day_later > 1:
        count_day = f"({day_later} days later)"


    if day is not None:
        temp1 = DAYS_OF_WEEK.index(day.capitalize())
        temp2 = temp1 + day_later
        if temp2 > 6:
            temp2 = temp2 % 7
            day = DAYS_OF_WEEK[temp2]
        else:
            day = DAYS_OF_WEEK[temp2]
        if count_day == "":
            return f"{str(result_hr)}:{str(result_min).zfill(2)} {period}, {day}"   
        else:
            return f"{str(result_hr)}:{str(result_min).zfill(2)} {period}, {day} {count_day}"    


    if count_day == "":
        return f"{str(result_hr)}:{str(result_min).zfill(2)} {period}"
    else:
        return f"{str(result_hr)}:{str(result_min).zfill(2)} {period} {count_day}"
