import sys

p=list('798512                                                                          3')
# p=list('                                                                                 ')

callcount = 0

# consideration of a guess: cell n with value c versus puzzle q
def NotInRow(cell, c, q):
    row = int(cell/9)
    for rowCell in range(row*9, row*9 + 9):
        if not rowCell == cell and q[rowCell] == c: return False
    return True
    
    
def NotInColumn(cell, c, q):
    col = cell%9
    for rowCounter in range(9):
        colCell = col + rowCounter*9
        if not colCell == cell and q[colCell] == c: return False
    return True
    
def NotInBlock(cell, c, q):
    row = int(cell/9)
    col = cell%9
    blockrow = int(row/3)
    blockcol = int(col/3)
    base = blockrow * 27 + blockcol * 3
    for i in range(3):
        for j in range(3):
            blockCell = base + i*9 + j
            if not blockCell == cell and q[blockCell] == c: return False
    return True
    
def solver(q):

    global callcount
    
    callcount += 1
    if callcount % 1000 == 0: print(callcount)
    
    # cut to the chase if the puzzle is solved
    if not ' ' in q: 
        print('SOLVED!!!!!!!!!!!!!!!!!!!!!!!!')
        print(q)
        hn = []
        hc = []
        for i in range(81):
            if not q[i] in hc:
                hc.append(q[i])
                hn.append(1)
            else:
                ind = hc.index(q[i])
                hn[ind] += 1
        print(hc)
        print(hn)
        sys.exit(0)

        
    # g=[]
    c=['1','2','3','4','5','6','7','8','9']

    # Construct a possible guess and take it
    for cell in range(81):
        if q[cell] == ' ':
            for j in c:
                if NotInRow(cell, j, q) and NotInColumn(cell, j, q) and NotInBlock(cell, j, q):
                    qq = q.copy()
                    qq[cell] = j
                    # print(qq)
                    solver(qq)
                    
    
    # Construct the possible guesses list of (cell, list) tuples
    # noChoice = False
    # for i in range(81):
    #     l = []
    #     if q[i] == ' ':
    #         for j in c:
    #             if NotInRow(i, j, q) and NotInColumn(i, j, q) and NotInBlock(i, j, q):
    #                 l.append(j)
    #         g.append((i, l))
    #         if len(l) == 0: noChoice = True
    
    # print(noChoice)
    # print(g)
    
    # Now we have some state on noChoice
    # if noChoice: return

    # g might now be, for example:
    #   g[0] = (17, ['3', '4', '6'])
    #   g[1] = (43, ['1', '9'])
    # 
    # If we got here then all the open cells have at least one choice
    #   so loop over all those options and try and solve for each
    # for choice in g:
    #     index = choice[0]
    #     for charChoice in choice[1]:
    #         q[index] = charChoice
    #         solver(q.copy())

    # return
    
  
solver(p)
    
    
    
    
    
    
    
    
    
    
    
    
    
            
