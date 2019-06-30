x = input().split()
dictionary = {'H':'D','D':'H'}
print(x[1] if x[0]=='H' else dictionary[x[1]])
