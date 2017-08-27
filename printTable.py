def printTable(table):
  colWidths = [0] * len(table)
  for i in range(len(colWidths)):
    for j in range(len(table[i])):
      if len(table[i][j]) > colWidths[i]:
        colWidths[i] = len(table[i][j])
  # print(colWidths)

  for i in range(len(table[0])):
    row = ''
    for j in range(len(table)):
      row += table[j][i].rjust(colWidths[j]) + ' '
    print(row)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
