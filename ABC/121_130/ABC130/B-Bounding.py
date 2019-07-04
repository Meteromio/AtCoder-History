N, X = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
for i in range(N+1):
  if i >= 1 and i <= N:
    D.append(D[i-1]+L[i-1])
print(len([int(y) for y in D if int(y) <= X]))
