def set_all_bits(n):
  sum = 0
  for i in range(0, n, 1):
    sum += (2**i)
  return sum

def get_integer(prompt):
  get_n = int(input(prompt))
  return get_n

n = get_integer('설정할 비트 수는? ')
res = set_all_bits(n)
print(f'{n} 비트를 모두 1로 설정한 수는 {res} (0b{"1"*n}) 이다.')