from datetime import datetime, timedelta
today = datetime.now()

oneday = timedelta(days=3)
anotherday= today - oneday

day = timedelta(days=1)
someday= today - day

week = timedelta(weeks=4)
somedate= today - week

print("This day was: "+str(oneday)+" ago")
print("Yesterday was: "+str(someday))
print("This week was: "+str(somedate)+" ago")
print(str(today.year))
print(str(today.month))
print(str(today.day))
print(str(today.hour))
print(str(today.minute))
print(str(today.second))
print(str(today.microsecond))

birthday = input('Tell us when is your birthday (dd/mm/yyyy)')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday is: '+str(birthday_date))
