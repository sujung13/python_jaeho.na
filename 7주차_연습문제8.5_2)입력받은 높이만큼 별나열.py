def print_right_triangle(height):
  """
  입력된 높이만큼의 직각 삼각형을 오른쪽으로 기울도록 '*'을 출력하는 함수
  """
  for i in range(1, height + 1):
      print(" " * (height - i) + "*" * i)

# 사용자로부터 높이 입력 받기
height = int(input("높이? "))

# 오른쪽으로 기울도록 '*' 나열 출력
print_right_triangle(height)