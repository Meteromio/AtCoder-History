A,B,C = (int(x) for x in input().split())
if (A*C)<=B:
  print(C)
elif (A*C)>=B:
  print(int(B/A))
else:
  print(0)
