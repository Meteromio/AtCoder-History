A, B = map(int, input().split())
print('Yes' if 1 in [(A*B*c) % 2 for c in [1, 3, 5, 7, 9]] else 'No')
