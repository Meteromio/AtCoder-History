N = list(input())
print('Yes' if int(''.join(N)) % sum(map(int, N)) == 0 else 'No')
