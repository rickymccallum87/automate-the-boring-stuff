def commaDelimited(l):
  commaList = ''
  for i in range(len(l)):
    if len(l) == 1:
      commaList += 'and ' + l[0]
    else:
      commaList += l[0] + ', '
      del l[0]
  return commaList

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaDelimited(spam))
