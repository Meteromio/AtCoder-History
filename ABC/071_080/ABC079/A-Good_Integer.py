import collections
N = list(input())
i = 0
result = 0
tmp = 0
for x in N:
  if tmp == x:
    result += 1
  tmp = x
  i += 1
count_n = collections.Counter(N)
print('Yes' if result >= 2 and count_n.most_common()[0][1] > 2  else 'No')