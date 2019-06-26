import collections
A,B,C = map(int, input().split())
print(collections.Counter([A,B,C]).most_common()[1][0])