S = list(input())
YY = int(''.join(S[:2]))
MM = int(''.join(S[2:]))

if MM == 0 or YY == 0:
  print("NA")
elif (YY<=12 and MM <=12):
  print("AMBIGUOUS")
elif (YY>=1 and MM <=12):
  print("YYMM")
elif (MM>=1 and YY >=1):
  print("MMYY")
else:
  print("NA")
