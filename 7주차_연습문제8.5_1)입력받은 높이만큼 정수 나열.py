def print_left_triangle(height):
  """
  입력된 높이만큼의 직각 삼각형을 왼쪽으로 기울도록 출력하는 함수
  """
  for i in range(1, height + 1):
      for j in range(1, i + 1):
          print(j, end='')
      print()

# 사용자로부터 높이 입력 받기
height = int(input("높이? "))

# 왼쪽으로 기울도록 정수 나열 출력
print_left_triangle(height)