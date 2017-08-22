print('I bet you I can count from any number to any higher number!')
rangeStart = int(input('Where should I start? '))
rangeEnd = int(input('Where should I stop? '))

count = ''
if rangeEnd - rangeStart < 10:
  for i in range(rangeStart, rangeEnd):
    count += str(i) + ', '
  print('That\'s easy: ' + count + str(rangeEnd) + '!! Told ya I could do it!')
else:
  for i in range(rangeStart, rangeStart + 5):
    count += str(i) + ', '
  print('Let\'s see. ' + count + 'umm.. This is gonna take forever. Forget it.')
