N = int(input())
town_names = dict()
assessments = []
for x in range(N):
  if x!=N:
    SP = input().split()
    assessments.append(SP[1])
    town_names.setdefault(SP[0],[]).append(assessments.index(SP[1])+1)
  else:
    break
result = []
for t in sorted(town_names):
  tmp = []
  for pointer in town_names[t]:
    tmp.append(assessments[pointer-1])
  for x in sorted(tmp, reverse=True,key=int):
    result.append(assessments.index(x)+1)
for x in result:
  print(x)
