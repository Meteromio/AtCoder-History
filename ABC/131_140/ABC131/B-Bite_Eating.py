N,L = map(int, input().split())
taste = [x+L for x in range(int(N))]

sum_taste = sum(int(x) for x in taste)
n_1_taste = [sum_taste-y for y in taste]
print(abs(sum_taste-n_1_taste[0]))
if sum_taste in n_1_taste:
  print(sum_taste)
elif L<0:
  print(min(n_1_taste))
else:
  print(max(n_1_taste))


# N,L = (int(x) for x in input().split())
# taste = []
# for x in range(int(N)):
#   taste.append(str(L+(x+1)-1))
# sum_taste = sum(int(x) for x in taste)
# n_1_taste = []
# t_taste= taste.copy()

# for y in t_taste:
#   taste.remove(str(y))
#   n_1_taste.append(sum(int(x) for x in taste))
#   taste.append(str(y))

# if sum_taste in n_1_taste:
#   print(sum_taste)
# elif L<0:
#   print(min(n_1_taste))
# else:
#   print(max(n_1_taste))
