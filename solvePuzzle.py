import numpy as np

def getPossible(p, r, c):
    ans = []
    sq = (r // 3, c // 3)
    sq_set = set(p[sq[0]*3:sq[0]*3+3, sq[1]*3:sq[1]*3+3].flatten())
    rowset = set(p[r, :])
    colset = set(p[:, c])
    return set(range(1, 10)) - (sq_set | rowset | colset)

def solvePuzzle(p):
    for r in range(9):
        for c in range(9):
            if p[r, c] == 0:
                for n in getPossible(p, r, c):
                    p[r, c] = n
                    if r == 8 and c == 8:
                        return True
                    if not solvePuzzle(p):
                        p[r, c] = 0
                    else:
                        return True
                return False

if __name__ == "__main__":
    test = [[0,0,0,6,0,4,7,0,0],
            [7,0,6,0,0,0,0,0,9],
            [0,0,0,0,0,5,0,8,0],
            [0,7,0,0,2,0,0,9,3],
            [8,0,0,0,0,0,0,0,5],
            [4,3,0,0,1,0,0,7,0],
            [0,5,0,2,0,0,0,0,0],
            [3,0,0,0,0,0,2,0,8],
            [0,0,2,3,0,1,0,0,0]]
    t = np.array(test)
    solvePuzzle(t)
    print(t)
