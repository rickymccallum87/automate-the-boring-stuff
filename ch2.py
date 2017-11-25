import sys, random

bool_val = int(input('0 or 1? '))
if bool_val != 0 and bool_val != 1:
	print('Get serious.')
	sys.exit()
elif bool_val:
	print('True talk!')
else:
	print('Falsetto? You bet-to.')

user = ''
while user != 'stop':
	user = input('Who is this? ')
	if user == 'Ricky':
		print('Cthulhu ftaghn, bro!')
	elif user == 'Kate':
		print('Sup, Pabodie lady?')
	elif user == 'Elise':
		print('Psh. Go back to R\'lyeh.')

for i in range(1,10):
	if bool_val and i % 2 == 0:
		continue
	print('1-' + str(i) + ': ' + str(random.randint(1,i)))
