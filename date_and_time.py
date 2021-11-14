import datetime

# date related
dt = datetime.datetime
dt_now = dt.now()
dt_today = dt.today()
set_date = dt(1978, 1, 26, 1, 25, 00, 0000)
day, month, year = dt_today.day, dt_today.month, dt_today.year

# time related
d_time = datetime.time()
set_time = datetime.time(11, 24, 33)

# sritptime()

# strftime()

# timestamp()


print("today is,", dt_now)
print("now is,", dt_today)
print("current year is,", dt_now.year)
print("I was born on,", set_date)
print('{}.{}.{}.'.format(day, month, year))
print(d_time)
print("set time is,", set_time)
# backslash "\" for splitting long line of code for readability
print("hour = {}, minute = {}, secede = {}, microsecond = {}" \
      .format(set_time.hour, set_time.minute, set_time.second, set_time.microsecond))
