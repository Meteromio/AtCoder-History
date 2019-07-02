n = int(input())
p = input().split()
i = 1
result = 0
while p:
  if (i+1)<n:
    if sorted([int(p[i-1]),int(p[i]),int(p[i+1])])[1] == int(p[i]):
      result+=1
    i+=1
  else:
    break
print(result)