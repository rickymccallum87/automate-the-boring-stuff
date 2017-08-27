inventory = {'torch': 6, 'rope': 3, 'gold': 88}
loot = ['gold', 'dagger', 'gold', 'gold', 'rope']

def displayInventory(inv):
  print('Inventory:')
  total = 0
  for k, v in inv.items():
    print(v, k)
    total += v
  print('Total number of items:', total)

def addToInventory(inv, loot):
  for i in range(len(loot)):
    inv.setdefault(loot[i], 0)
    inv[loot[i]] += 1
  return inv

displayInventory(inventory)
print('\nYou defeated a dragon!\n')
inventory = addToInventory(inventory, loot)
displayInventory(inventory)
