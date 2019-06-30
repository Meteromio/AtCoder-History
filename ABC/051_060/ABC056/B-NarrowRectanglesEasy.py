W,a,b = map(int, input().split())
if (b+W)-a<=0:
  print(-((b+W)-a))
elif b-(a+W)<=0:
  print(0)
else:
  print(b-(a+W))
