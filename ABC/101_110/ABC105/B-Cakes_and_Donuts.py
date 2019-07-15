N = int(input())
tmp = []
for i in range(10):
  for j in range(10):
    solve = (4*(i+1))+(7*(j+1))
    if solve <= 100:
      tmp.append(solve)
multiples = sorted(list(set(tmp)))

if N % 4 == 0 or N % 7 == 0 or N in multiples:
  print("Yes")
else:
  print("No")

  # tmp = N - (N % 4) * 4
  # if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
  #   print("Yes")
  # elif tmp % 11 == 0 or tmp % 7 == 0 or tmp % 4 == 0:
  #   print("Yes")
  # else:
  #   print('No')
# N = int(input())
# tmp = N - (N % 4) * 4
# if N % 4 == 0 or N % 7 == 0 or N % 11  == 0:
#   print("Yes")
# elif tmp % 11 == 0 or tmp % 7 == 0 or tmp % 4 == 0:
#   print("Yes")
# else:
#   print('No')
