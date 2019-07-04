N = int(input())
W = list(map(int, input().split()))
result = []
for x in range(N):
  result.append(abs(sum(W[0:x])-sum(W[x:])))
print(min(result))