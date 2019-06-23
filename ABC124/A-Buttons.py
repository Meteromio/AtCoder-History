list_ab = [int(x) for x in input().split()]
dict_ab = [x for x in list_ab]
result = 0
for y in range(2):
  dic_max_i = max(dict_ab)
  result = result + dic_max_i
  dict_ab.remove(dic_max_i)
  dict_ab.append(dic_max_i-1)
print(result)
