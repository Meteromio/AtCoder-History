X = input().split()
formulas = []
formulas.append(''.join(X[0]+X[1]+"+"+X[2]))
formulas.append(''.join(X[1]+X[2]+"+"+X[0]))
formulas.append(''.join(X[2]+X[0]+"+"+X[1]))
print(max([eval(x) for x in formulas]))