N = int(input())
values = list(map(int,input().split()))
costs = list(map(int,input().split()))
dictionary = []
for v in range(N):
  dictionary.append([values[v],costs[v]])
x,y=0,0
result = []
for i in range(N):
  if dictionary[i][0] - dictionary[i][1]>0:
    result.append(dictionary[i][0]-dictionary[i][1])
print(sum(result))

# 解けなかったので回答を見て理解した
# 気づけたのは v < c だった場合はだめってこと、
# もう一つ必要だったのが、 v - c が 1以上であることだった。これがなかった