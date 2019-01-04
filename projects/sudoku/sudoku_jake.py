# index on [0, 80] produces lists of indices for that row / column / block

def row_indices(i): return range(i - i % 9, i - i % 9 + 9)

def col_indices(i): return range(i % 9, i % 9 + 81, 9)

def box_indices(i):
    start = 27 * (i // 27) + 3 * ((i % 9) // 3)
    return [i for j in range(3) for i in range(start + 9 * j, start + 9 * j + 3)]

# connected[] is a list of sets { ... }, in fact 81 of them where the list index is the cell index
#   The set for a given index is a set that is the union of three sets... rule-connect cell indices...
#     ...with the index i itself excluded
connected = [(set.union(set(box_indices(i)), set(row_indices(i)), set(col_indices(i))) - set([i]))
             for i in range(81)]

solution_count = 0

# solver(p) will recursively find solutions and "yield" them
#   A key idea here is that the 'p' this is passed the first time is a precise copy of the original puzzle
#   but subsequent (recursive) calls to solver() will provide guess-versions of the puzzle that have
#   additional squares filled in. In this way eventually solver(p) will be -- we hope -- passed a complete
#   solution built up from the original puzzle. When this happens there are two logical paths for the
#   code:
#     Test for this immediately; and celebrate!
#     Build a picture of possible moves first; then test and *yield*
def solver(p):

    global solution_count
    if '0' not in p:
        print('found', solution_count, ':', p)
        solution_count += 1
        if solution_count > 20: return

    
    # Accumulate a list L[] of triples across empty squares
    #   Each triple is(number of possible guesses, this square index, a set of those guesses)
    L = []
    for i in range(81):
        if p[i] == '0':
            vals = set('123456789') - set(p[n] for n in connected[i])
              # working backwards: connected[i] is a set of related cells to cell i
              #   For example for i = 10 we have these connected cell indices:
              #   { 0,1,2,9,10,11,12,13,14,15,16,17,18,19,20,28,37,46,55,64,73}
              #   for n in connected[i] has n scan all these puzzle indices: 0,1,2,9,...,73
              #   p[n] is the puzzle value at that index, e.g. '0' or '3' or '4'
              #   set() makes a set of these puzzle values without any duplicates
              #   set('123456789') - set() removes these puzzle values from the set
              #     of allowed guesses; producing a set of properly constrained allowed guesses.
              # vals is a set of legal guesses for this square in this call of solver()
            if len(vals) == 0: return
              # if solver has found a square with no legal guesses it simply returns None
              #   We want to bail out of solver() if a cell is a dead end
            else: L.append((len(vals), i, vals))
              # otherwise contribute to the L[] list of triples as described above
    
    # if all squares are solved, then yield the current solution
    #   Notice this is done only *after* L is constructed... why???
    if len(L) == 0 and '0' not in p: yield p
        
    # choose a cell (index) with the smallest number of possibles; recursively call S() for each possible
    else:
        N, i, vals = min(L)   # that is a triple based on the first minimum N in L[]
        for val in vals:      # try all possible allowed guesses for this cell...
            for s in solver(p[:i] + val + p[i + 1:]): yield s  # ...and for each return all solutions

p0 = '000000000000000000000000000000000000000000000000000000000000000000000000000000000'
p1 = '060000008201800500905002000000704602300090005504608000000900301007005906100000050'

allsolns = solver(p0)
for a in allsolns: print(a)
