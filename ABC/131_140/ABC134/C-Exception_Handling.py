N = int(input())
As = [int(input()) for _ in range(N)]
Bs = sorted(As)
for x in As:
  if x == Bs[-1] and x != Bs[-2]:
    print(Bs[-2])
  else:
    print(Bs[-1])
