day = input().strip()
k = int(input())

day_mapper = {
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 7
}

mapper_day = {
    1 : "Monday",
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    0 : "Sunday"
}

total_days = day_mapper.get(day) + k
current_day = total_days%7

print(mapper_day.get(current_day))
