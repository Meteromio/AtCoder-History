card_power = {'2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8','10':'9','11':'10','12':'11','13':'12',"1":'13'}
A,B = input().split()
if int(card_power[A]) == int(card_power[B]):
  print('Draw')
elif int(card_power[A]) > int(card_power[B]):
  print('Alice')
elif int(card_power[A]) < int(card_power[B]):
  print('Bob')
