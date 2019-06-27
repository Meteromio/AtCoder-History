N = int(input())
A = int(input())
if A == 0 and N%500==1:
  print('No')
elif A - (N%500) < 0:
  print('No')
else:
  print('Yes')