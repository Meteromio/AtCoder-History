As = input().split()
result =  int(max(As)) - int(min(As))
print(-result if result<0 else result)