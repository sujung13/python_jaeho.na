def exchange(n):
  n500 = n // 500
  n100 = (n % 500) // 100
  n50 = (n % 100) // 50
  n10 = (n % 50) // 10
  return n500, n100, n50, n10

def get_integer(prompt):
  get_n = int(input(prompt))
  return get_n

n = get_integer('동전으로 교환하고자 하는 금액은? ')
n500, n100, n50, n10 = exchange(n)
print('500원 동전의 개수: ', n500)
print('100원 동전의 개수: ', n100)
print('50원 동전의 개수: ', n50)
print('10원 동전의 개수: ', n10)