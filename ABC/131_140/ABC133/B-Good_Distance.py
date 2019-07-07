import numpy as np
N, D = map(int, input().split())
Xs = []
while True:
  Xs.append(list(map(int, input().split())))
  if len(Xs) == N:
    break
result = []
tmp = []
for x in Xs:
  tmp.append(x)
  for n in range(N):
    if Xs[n] in tmp:
      l = np.linalg.norm(np.array(x) - np.array(Xs[n]))
      if l.is_integer() and l > 0:
        result.append(l)
print(int(len(result)))
