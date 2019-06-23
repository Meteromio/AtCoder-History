a,b = input().split()
a_i = int(a)
b_i = int(b)
if a_i>=13:
  print(b_i)
elif a_i>=6 and a_i<13:
  print(int(b_i/2))
elif a_i<6:
  print(0)