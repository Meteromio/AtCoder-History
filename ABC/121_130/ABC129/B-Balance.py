N = int(input())
W = list(map(int, input().split()))
print(min([abs(sum(W[0:x])-sum(W[x:])) for x in range(N)]))
