from datetime import date
now = date.today()
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1996, 9, 23)
age = now - birthday
print age.days
