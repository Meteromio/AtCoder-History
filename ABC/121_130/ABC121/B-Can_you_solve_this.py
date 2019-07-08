N, M, C = map(int, input().split())
Bs = list(map(int, input().split()))
As = [list(map(int, input().split())) for _ in range(N)]
cr = 0
code_result = 0
for a in As:
  for i in range(M):
    code_result += a[i] * Bs[i]
  if code_result + C > 0:
    cr += 1
  code_result = 0
print(cr)
