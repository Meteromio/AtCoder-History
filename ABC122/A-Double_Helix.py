enki_a = ['A','T']
enki_b = ['C','G']

b = input()

if b in enki_a:
  enki_a.remove(b)
  print(''.join(enki_a))
elif b in enki_b:
  enki_b.remove(b)
  print(''.join(enki_b))