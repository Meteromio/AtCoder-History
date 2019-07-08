N = int(input())
Xs = [list(map(str, input().split())) for _ in range(N)]
one_BTC = 380000.0
otoshidama = 0
for x in Xs:
  if x[1] == "JPY":
    otoshidama += int(x[0])
  else:
    otoshidama += (float(x[0])*one_BTC)
print(otoshidama)