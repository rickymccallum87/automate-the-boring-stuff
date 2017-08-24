def collatz(number):
  if number % 2 == 0:
    new = number // 2
  else:
    new = number * 3 + 1
  print(new)
  return new

number = int(input('Enter an integer: '))

while number != 1:
  number = collatz(number)
