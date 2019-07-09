N = int(input())
Ps = [list(map(int, input().split())) for _ in range(N)]
max_p = max(Ps)
Ps.remove(max_p)
Ps.append([max_p[0]//2])
r = 0
for p in Ps:
  r += p[0]
print(r)