N = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
A,B = input().split()
if N[A] < N[B]:
  print('<')
elif N[A] > N[B]:
  print('>')
else:
  print('=')