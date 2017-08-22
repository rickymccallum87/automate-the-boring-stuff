print('It\'s time to launch the shuttle!')
start = int(input('What should I count down from? '))

countdown = ''
for i in range(start, 0, -1):
  countdown += str(i) + '.. '
print(countdown + 'We have lift off!!')
