N = int(input())
for x in range(999):
  if str(N).count(list(str(N))[0]) == 3:
    print(N)
    break
  else:
    N += 1
