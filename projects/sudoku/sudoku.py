import sys

count = 0

p1 = '060000008201800500905002000000704602300090005504608000000900301007005906100000050'

all = ['1','2','3','4','5','6','7','8','9']

def rowlist(r):
    return ['1', '2']

def collist(c):
    return ['1', '2']

def blocklist(b):
    return ['1', '2']

def getrow(i): return int(i/9)

def getcol(i): return i%9

def getblock(i):
    
def ok(i):
    r = rowlist(getrow(i))
    c = collist(getcol(i))
    b = blocklist(getblock(i))
    a[:] = all[:]
    return([a[i] for i in range(9) if a[i] not in r and a[i] not in c and a[i] not in b])
   
def solver(p):
    global count
    count += 1
    if count % 1000 == 0: print(count)
    for i in len(p):
        if p[i] == '0':
    

                    

    
  
solver(p1)
    
    
    
    
    
    
    
    
    
    
    
    
    
            
