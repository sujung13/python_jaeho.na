exchange_rate = 0

def set_rate(won):
  global exchange_rate
  exchange_rate = won

def get_rate():
  return exchange_rate

def to_dollar(won):
  return won / exchange_rate

def to_won(dollar):
  return dollar * exchange_rate

def main():
  print('###환율 변환 모듈 테스트###')
  print('오늘의 환율 ', end = '')
  set_rate(int(input()))
  
  won = 2020
  dollar = to_dollar(won)
  print(f'{won} 원= {dollar} 달러')
  dollar = 2
  won = to_won(dollar)
  print(f'{dollar} 달러 = {won} 원')

if __name__ == "__main__":
  main()