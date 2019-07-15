N = int(input())
S = list(input())
r = []
c = 0
for x in range(N):
  for y in set(S[:x]):
    if y in S[x:]:
      c += 1
  r.append(c)
  c = 0
print(max(r))