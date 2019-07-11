N = int(input())
Ws = []
for x in range(100):
  Ws.append(str(input()))
  if x+1 == N:
    break

words = [Ws[0]]
tmp = list(Ws[0])[-1]
Ws.remove(Ws[0])

for y in Ws:
  if y in words:
    print('No')
    break
  elif tmp == list(y)[0]:
    words.append(y)
    tmp = list(y)[-1]
  else:
    print('No')
    break

if len(words) == N:
  print('Yes')
