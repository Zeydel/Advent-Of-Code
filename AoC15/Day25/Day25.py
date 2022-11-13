def getIndex(row, column):
    t = (column*(column+1))/2
    print(t)
    t2 = ((row*(row-1))/2)
    print(t2)
    return t+(t2*(column-1))

f = open('input.txt', 'r')
presents = f.read().split(' ')

row = int(presents[16][:-1])
column = int(presents[18][:-1])