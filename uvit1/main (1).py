def isleapyear(year):
  if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
    return True

year = 2000
if isleapyear(year):
  print('{} is a leapyear.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))
  