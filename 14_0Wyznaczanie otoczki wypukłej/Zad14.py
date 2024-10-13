# Skończone
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.is_r = False
    
    def __repr__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not (self.x == other.x and self.y == other.y)


def jarvis_1(points):
    if len(points) < 3: 
        return points
    
    idx = points.index(min(points))
    p = points[idx]
    
    convex_hull = [p]
    q = points[idx + 1]
    
    while 1:
        for r in points:
            if (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x) > 0:
                q = r
        if q == convex_hull[0]:
            break
        
        if q != convex_hull[-1]:
            convex_hull.append(q)
        p = q
        idx += 1
        q = points[(idx + 1) % len(points)]
    
    return convex_hull


def distance(a,b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def jarvis_2(points):
    if len(points) < 3: 
        return points
    
    idx = points.index(min(points))
    p = points[idx]
    
    convex_hull = [p]
    q = points[idx + 1]
    
    while 1:
        for r in points:
            if (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x) > 0:
                q = r
            if (q.y - p.y)*(r.x - q.x) - (r.y - q.y)*(q.x - p.x) == 0\
            and distance(p, r) * 0.99 < distance(p, q) + distance(q, r) \
            < distance(p, r) * 1.01:
                q = r
        if q == convex_hull[0]:
            break
        
        if q != convex_hull[-1]:
            convex_hull.append(q)
        p = q
        idx += 1
        q = points[(idx + 1) % len(points)]
    
    return convex_hull
    
    

def main():
    points = []
    for i in [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]:
        points.append(Point(i[0], i[1]))
    print(jarvis_1(points))
    print(jarvis_2(points))
    

main()