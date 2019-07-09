import collections
s = int(input())
result = [s]
tmp = s
while True:
  if collections.Counter(result).most_common()[0][1] == 2:
    break
  elif tmp%2 == 0:
    x = tmp/2
  elif tmp%2 > 0:
    x = (3*tmp) + 1
  tmp = x
  result.append(int(x))
print(len(result))