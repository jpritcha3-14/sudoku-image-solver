import cv2
import argparse
import os
import re

import numpy as np
import matplotlib.pyplot as plt

from getPoints import getSquare
from coordTransform import coordTransform
from templateMatch import parseSquares, parseSumsNums, createSquareMask

def ingest(files, outdir):
    offset  = 5

    getnum = re.compile('^\d+')
    nextFileNum = 0
    if len(os.listdir(outdir)) > 1:
        nextFileNum = 1 + max(int(re.match(getnum, f).group(0)) for f in os.listdir(outdir))

    for f in files:
        if os.path.exists(f):
            src = cv2.imread(f)
            pts, src = getSquare(src, offset)
            tformed = coordTransform(src, pts, 306 + 2*offset)
            tformed = tformed[:, :, np.newaxis] 
            tformed = np.concatenate((tformed, tformed.copy(), tformed.copy()), axis=2)
            parsedSquares = parseSquares(tformed, createSquareMask(34, 2), offset)
            parsedSums, _ = parseSumsNums(tformed, parsedSquares)
            for r in range(9):
                for c in range(9):
                    if parsedSums[r][c] > 50000:
                        x, y = parsedSquares[r][c]
                        cur = tformed[y:y+34, x:x+34]
                        print('writing:', os.path.join(os.getcwd(), outdir, str(nextFileNum) + '.png'), end=": ")
                        if cv2.imwrite(os.path.join(os.getcwd(), outdir, str(nextFileNum) + '.png'), cur):
                            print('Success!')
                            nextFileNum += 1
                        else:
                            print('Failure!')
            os.rename(os.path.join(os.getcwd(), f) , os.path.join(os.getcwd(), f + '_ingested'))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('outdir', nargs=1)
    ap.add_argument('files', nargs='+')
    args = vars(ap.parse_args())
    print(args['files'])
    ingest(args['files'] ,args['outdir'][0]) 
