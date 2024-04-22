def convert_time(s):
  h = s // 3600
  m = (s - h*3600) // 60
  s = s % 60
  return h, m, s

def get_integer(prompt):
  n = int(input(prompt))
  return n

second = get_integer('변환하고자 하는 시간(초)? ')
h, m, s = convert_time(second)
print(f'{second} 초는 {h} 시간 {m}분 {s} 초이다.')