N = int(input())
heights = list(map(int,input().split()))
result = []
i = 1
for x in range(N):
  if x==0:
    result.append(1)
  elif i<len(heights) and heights[x] <= heights[i] and heights[i-1] <= heights[i]:
    print("in")
    result.append(1)
  i+=1
print(result)