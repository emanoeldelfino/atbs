def printTable(lists):
    # for lista in lists:
    #     for item in lista:
    #         print(item.rjust(10), end='')
    #     print()

    colWidths = [0] * len(lists)

    for i in range(len(lists)):
        colWidths[i] = len(max(lists[i], key=lambda string: len(string)))

    columLen = max(colWidths)

    for i in range(len(lists[0])):
        for lista in lists:
            print(lista[i].rjust(columLen), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
