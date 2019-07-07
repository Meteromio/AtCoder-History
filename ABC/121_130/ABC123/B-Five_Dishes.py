orders = [int(input()), int(input()), int(input()), int(input()), int(input())]
order_tmp = 0
result = []
for order in orders:
  if order %2 > 1:
    result += order + (10 - (order % 10))
  else:
    result += order
print(result)
