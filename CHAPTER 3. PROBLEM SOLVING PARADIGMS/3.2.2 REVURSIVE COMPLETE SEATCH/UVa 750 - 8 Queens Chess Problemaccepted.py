def write(s=None):
    f = open('output.txt','a')
    f.write((str(s)+'\n') if s is not None else '\n')

def readIntArr():
    return [int(x) for x in input().split()]

def readInt():
    return int(input())

def prf(s):
    write(s)

# global vars
a = 0 
b = 0
row = [0]*8
# the line counter
solCount = 0

# check if any row or diagonal has two queens on it
def check(r,c):
    for prev in range(c):
        if row[prev]==r or abs(row[prev]-r)==abs(prev-c):
            return False
    return True

# the recursion
def backtrack(c):
    global solCount
    global row
    global a,b

    if c==8 and row[b]==a:
        # candidate solution. print it
        solCount += 1
        print('{0:2}      {1}'.format(solCount, ' '.join([str(x+1) for x in row])))

    # generate all permutations and check
    for r in range(8):
        if check(r, c):
            row[c] = r
            backtrack(c+1)

def sol():
    global a,b
    a,b = readIntArr()

    # shift to 0-based indexing
    a-=1
    b-=1

    backtrack(0)

def main():
    global solCount
    t = readInt()
    input()
    
    for i in range(t):
        print('SOLN       COLUMN')
        print(' #      1 2 3 4 5 6 7 8')
        print()
        sol()
        if i<t-1:
            print()
            input()
            solCount = 0

main()
