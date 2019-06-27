X,A,B = map(int,input().split())
if B-A<=0:
  print("delicious")
elif X+1 <= B-A:
  print("dangerous")
else:
  print("safe")