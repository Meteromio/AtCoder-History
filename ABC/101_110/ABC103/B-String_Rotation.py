S = list(input())
T = input()
s_tmp = S.copy()
if ''.join(S) == T:
  print('Yes')
else:
  while True:
    s_reversed = s_tmp[:-1]
    s_reversed.insert(0, s_tmp[-1])
    if ''.join(s_tmp) == T:
      print('Yes')
      break
    elif S == s_reversed:
      print('No')
      break
    s_tmp = s_reversed
