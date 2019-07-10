N,T = map(int,input().split())
ct = [list(map(int, input().split())) for _ in range(N)]
cr = []
for x in range(N):
  if T >= ct[x][1]:
    cr.append(ct[x][0])
print('TLE' if len(cr) == 0 else min(cr))
