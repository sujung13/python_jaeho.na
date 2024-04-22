def fahrenheit_to_celsius(F):
  C = 5 / 9 * (F-32)
  return C

def get_real(prompt):
  F = int(input(prompt))
  return F

F = get_real('변환하고자 하는 화씨온도? ')
C = fahrenheit_to_celsius(F)
print(f'화씨 {F}도는 섭씨 {C}도')