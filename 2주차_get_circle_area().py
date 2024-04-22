def get_circle_area(prompt):
  r = int(input(prompt))
  area = 3.14*r*r
  return area

res = get_circle_area('원의 반지름은? ')
print(f'원의 넓이는? {res}')