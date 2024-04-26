def input_age(prompt):
  age = int(input(prompt))
  if 0 <= age <= 120:
    return age
  else:
    return -1

def is_adult(age):
  return age >= 19

age = input_age('나이? ')
if age != -1:
  if is_adult(age):
    print('당신은 성인입니다.')
  else:
    print('당신은 성인이 아닙니다')
else:
  print('오류: 유효하지 않은 나이가 입력되어 판별할 수 없습니다!')