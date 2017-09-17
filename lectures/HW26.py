from datetime import date
import time
import calendar

# 1.
weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for year in range(1950, 2018):
    if calendar.monthrange(year, 2)[1] == 29:
        print(year, "is a leap year. An January 1 at that year is", weekdays[calendar.weekday(year, 1, 1)])


# 2. 19500101 ~ 20171231
start = date(1950, 1, 1)
end = date(2017,12, 31)
days = abs(end - start)
print(days.days,"days passed")


# 3.
count = 0
for year in range(1950, 2018):
    for month in range(1, 13):
        if calendar.weekday(year, month, 13) == 4:
            count += 1

print("There have been", count, "times of Friday the 13th.")