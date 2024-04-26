def introduce(n, g):
  print(f'{n[1:]}은 내년에 {g + 1}학년입니다.')

#주 프로그램부
name = input('이름? ')
grade = int(input('학년? '))
introduce(name, grade)