def set_all_bits(n):
  return (2**n - 1)

def get_integer(prompt):
  get_n = int(input(prompt))
  return get_n

n = get_integer('설정할 비트 수는? ')
res = set_all_bits(n)
print(f'{n} 비트를 모두 1로 설정한 수는 {res} ({bin(res)}) 이다.')