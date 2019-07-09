S = list(input())
like_number = 753
i = 0
r = []
while True:
  if i == len(S):
    break
  elif len(S[i:3+i]) >= 3:
    c = int(''.join(S[0+i:3+i])) - like_number
    r.append(abs(c))
  else:
    break
  i += 1
print(min(r))
