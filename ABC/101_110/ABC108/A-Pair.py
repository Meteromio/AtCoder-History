K = int(input())
odds = []
evens = []
for x in range(K):
  x+=1
  if x%2 == 0:
    evens.append(x)
  else:
    odds.append(x)
print(len(evens)*len(odds))
