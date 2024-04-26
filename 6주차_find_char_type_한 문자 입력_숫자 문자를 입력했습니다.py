def find_char_type(char):
  if '0' <= char <= '9':
      return "숫자문자를 입력했습니다."
  elif 'A' <= char <= 'Z' or 'a' <= char <= 'z':
      return "알파벳문자를 입력했습니다."
  elif char == ' ':
      return "공백문자를 입력했습니다."
  else:
      return "기타문자를 입력했습니다."

# 사용자로부터 문자 입력 받기
while True:
  user_input = input("한 문자 입력? ")

  # 입력이 없을 경우 종료
  if not user_input:
      break

  # 첫 번째 문자만 고려
  char = user_input[0]

  # 문자의 종류 출력
  print(find_char_type(char))
