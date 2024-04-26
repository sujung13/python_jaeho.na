def is_leap_year(year):
  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    return True
  else:
    return False

while True:
  year = int(input("윤년 여부를 확인할 연도는? "))
# 입력이 없을 경우 종료
# if not year:
  # break

# 윤년 여부 판별 후 출력
  if is_leap_year(year):
    print(f" {year}년은 윤년입니다.")
  else:
    print(f" {year}년은 평년입니다.")

  # 다른 연도도 확인할 것인지 묻기
  answer = input("다른 연도도 확인하겠습니까? ")
  if (answer != 'Y') and (answer != 'y'):
    break