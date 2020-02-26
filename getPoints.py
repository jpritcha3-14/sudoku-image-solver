import cv2
import argparse
import numpy as np

def selectPoint(event, x, y, flags, params):
    cpy, points, maxPoints = params
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < maxPoints:
        points.append([x-2,y-2])
        cv2.rectangle(cpy, (x-7, y-7), (x+3, y+3), color=(0, 255, 0))
    
def _getPoints(img, numPoints):
    cpy = img.copy()
    points = []
    cv2.namedWindow("image")
    cv2.setMouseCallback(
            "image", 
            selectPoint, 
            [cpy, points, numPoints])
    
    while True:
        cv2.imshow("image", cpy)
        key = cv2.waitKey(1) & 0xFF
    
        if key == 13 and len(points) == numPoints:
            break
        
        if key == ord("c"):
            points.clear()
            cpy = img.copy()
            cv2.setMouseCallback(
                    "image", 
                    selectPoint, 
                    [cpy,  points, numPoints])

    return points

def getPoints(img, numPoints):
    return tuple(map(tuple, getPoints(img, numPoints)))

def getSquare(img, offset=0):
    # Sort 4 srcPts into row, column order
    pts = _getPoints(img, 4)
    pts.sort(key = lambda x: x[0]**2 + x[1]**2)
    pts2 = sorted(pts[1:3], key = lambda x: x[1])
    pts2.insert(0, pts[0]) 
    pts2.append(pts[-1]) 

    # Add offset to 4 corners
    for i, p in enumerate(pts2):
        p[0] = p[0] + (offset if i % 2 else -offset)
        p[1] = p[1] + (offset if i > 1 else -offset)
    return tuple(map(tuple, pts2))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", 
            required = True, 
            help = "Path to image")
    ap.add_argument("-p", "--points", 
            required=False, default=4,  
            help="Number of points to capture")
    args = vars(ap.parse_args())

    print(getPoints(cv2.imread(args["image"]), int(args["points"])))
