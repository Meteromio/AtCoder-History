S = list(input())
acgt = ['A', 'C', 'G', 'T']
lengths = []
l = 0
for x in S:
  if x in acgt:
    l += 1
  else:
    lengths.append(l)
    l = 0

if len(lengths) == 0 or l > 0:
  lengths.append(l)

print(max(lengths))
