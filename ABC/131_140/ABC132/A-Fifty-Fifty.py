import collections
S = list(input())
print('Yes' if len(collections.Counter(S).keys())==2 and list(collections.Counter(S).values())[0]==2 else 'No')