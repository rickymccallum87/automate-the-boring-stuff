#! pw.py - An insecure password locker program.

PASSWORDS = {'email': 'turkey darn lift',
             'blog': 'valve smiley barbell',
             'luggage': '12345'}

import sys

if len(sys.argv) < 2:
  print('Usage: python pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1] # first command line argument is the account name

print(account)

if account in PASSWORDS:
  print('Password for ' + account + ' copied to clipboard.')
else:
  print('There is no account named ' + account)
