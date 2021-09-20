import numpy as np
def area(p1, p2, p3): 
    # converting to an area
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def isInside(a, b, c, p): 
    
    #checking area 
    A = area (a, b, c) 
  
    
    A1 = area (b, c, p) 
      
    # Calculate area of triangle PAC  
    A2 = area (a, c, p) 
      
    # Calculate area of triangle PAB  
    A3 = area (b, a, p) 
      
    # Check if sum of A1, A2 and A3  
    # is same as A 
    return A == A1 + A2 + A3

def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    # Write your code here
    # check if both are inside the area of the given points 
    # draw the graph? 
    #creating points for reusability
    a,b,c, p, q=(x1,y1), (x2,y2), (x3,y3), (xp,yp), (xq,yq)
    #drawing the triangle 
    ab = np.linalg.norm([a[0]-b[0],a[1]-b[1]])
    bc = np.linalg.norm([c[0]-b[0],c[1]-b[1]])
    ac = np.linalg.norm([a[0]-c[0],a[1]-c[1]])

    #
    output = 0
    #checking if it is a triangle 
    if ab+bc>ac and bc+ac > ab and ab+ac>bc:
        # checking for inside points
        if isInside(a, b, c, p) and isInside(a, b, c, q):
            output = 3
        elif isInside(a, b, c, p):
            output = 1
        elif isInside(a, b, c, q):
            output = 2
        else:
            output = 4
    return output