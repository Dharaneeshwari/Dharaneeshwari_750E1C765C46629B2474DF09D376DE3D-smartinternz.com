def isLeapYear (year):
  if (year % 40 and year %100 != 0):
     return True
  else:
      return False

year = int(input("Enter a year: "))
if isLeapYear (year):
  print('{} is a leap year'.format(year))
else:
  print('{} is not a leap year'.format(year))