N, X = map(int, input().split())
L = [int(x) for x in input().split()]
D = []
i = 0
while N+1:
  if i == 0:
    D.append(0)
  elif i<=N:
    D.append(D[i-1]+L[i-1])
  else:
    break
  i+=1
#print(D)
print(len([int(y) for y in D if int(y)<=X]))