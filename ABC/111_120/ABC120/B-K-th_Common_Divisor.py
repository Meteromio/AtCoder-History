A,B,K = map(int,input().split())
result = []
for x in range(A):
  if A%(x+1) == 0 and B%(x+1) == 0:
    result.append(x+1)
print(result[-K])
