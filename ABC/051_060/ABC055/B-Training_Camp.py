N = int(input())
power = 1
for x in range(N):
  power = (power * (x+1))%(10**9+7)
print(power)
