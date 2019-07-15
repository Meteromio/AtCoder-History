N = int(input())
As = list(map(int,input().split()))
r = []
for x in range(N):
  for y in range(x+1, N):
    r.append(abs(As[x]-As[y]))
print(max(r))