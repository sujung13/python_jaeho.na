def is_year_leap(y):
  if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    return '윤년'
  else:
    return '평년'

def month_days(y, m):
  if m == 2:
    if y == '윤년':
      return '29'
    else:
      return '28'
  if (m <= 7 and m % 2 != 0) or (m > 7 and m % 2 == 0):
    return '31'
  else:
    return '30'
    
# 주 프로그램
year = int(input('연도? '))
month = int(input('월? '))
year_leap = is_year_leap(year)
m = month_days(year_leap, month)
print(f'{year}년 {month}월은 {m}까지 있습니다.')