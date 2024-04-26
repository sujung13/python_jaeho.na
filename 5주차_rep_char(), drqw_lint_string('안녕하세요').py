def rep_char(c, n):
  print(c * n)

def draw_line_string(prompt):
  rep_char('-', len(prompt)*2)
  print(prompt)
  rep_char('-', len(prompt)*2)
          
draw_line_string('안녕하세요')