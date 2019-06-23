n,k = input().split()
s = list(input())
s[int(k)-1] = s[int(k)-1].lower()
print(''.join(s))