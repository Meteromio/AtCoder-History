S = input()
result = 0
for x in ['a','b','c']:
  if x in S:
    result+=1
print('Yes' if result==3 else 'No')