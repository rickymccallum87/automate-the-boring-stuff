inventory = {'torch': 6, 'rope': 3, 'gold': 88}

def displayInventory(inv):
  print('Inventory:')
  total = 0
  for k, v in inv.items():
    print(v, k)
    total += v
  print('Total number of items:', total)

displayInventory(inventory)
