a, b, c, d = map(int, input().split())
m = [a-b, a-c, b-c]
mr = []
for x in m:
  if x<0:
    mr.append(-x)
  else:
    mr.append(x)

if mr[0] <= d and mr[2] <= d:
  print("Yes")
elif mr[1] <= d:
  print("Yes")
else:
  print("No")