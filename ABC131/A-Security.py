S = list(input())
s_list = []
index = 0
result = "Good"
for x in S:
  if index == 0:
    s_list.append(x)
    index+=1
  else:
    if s_list[index-1] == S[index]:
      result = "Bad"
    else:
      s_list.append(x)
      index+=1
print(result)

