O = list(input())
E = list(input())
i = 1
for x in E:
  O.insert(i,x)
  i+=2
print(''.join(O))