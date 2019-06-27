x,a,b = map(int,input().split())
x_a = a-x
x_b = b-x
if x_a < 0:
  x_a = -x_a
if x_b < 0:
  x_b = -x_b
print('A' if x_a < x_b else 'B')
