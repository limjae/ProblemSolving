from collections import defaultdict
from collections import deque

def solution(board):
    answer = 0
    visitdict = defaultdict(set)
    visitqueue = deque()
    n = len(board)
    dp = [[0,1], [0,-1], [1,0], [-1,0]]

    y1, x1, y2, x2 = 0, 0, 0, 1
    p1 = pointOf(y1, x1)
    p2 = pointOf(y2, x2)

    visitdict[p1].add(p2)
    visitdict[p2].add(p1)

    visitqueue.append([p1, p2, 0])
    visitqueue.append([p2, p1, 0])

    dh = [1, -1]


    while visitqueue:
        p1, p2, m = visitqueue.popleft()
        # print(p1, p2, m)
        y1, x1 = xypoint(p1)
        y2, x2 = xypoint(p2)
        if (y1 == n-1 and x1 == n-1) or (y2 == n-1 and x2 == n-1):
            return m

        for d in dp:
            dy, dx = d
            pvia = pointOf(y2+dy, x2+dx)
            pto = pointOf(y1+dy, x1+dx)
            if movable(y2+dy, x2+dx, y1+dy, x1+dx, n, board) and pto not in visitdict[pvia]:
                visitdict[pvia].add(pto)
                visitdict[pto].add(pvia)
                visitqueue.append([pvia, pto, m+1])
                visitqueue.append([pto, pvia, m+1])

        #spin
        if ishorizon(p1, p2):
            # pfix = p1, pmove = p2
            pvia = pointOf(y2+1, x2)
            pto = pointOf(y1+1, x1)
            if movable(y2+1, x2, y1+1, x1, n, board) and pto not in visitdict[p1]:
                visitdict[p1].add(pto)
                visitdict[pto].add(p1)
                visitqueue.append([p1, pto, m+1])
                visitqueue.append([pto, p1, m+1])

            pvia = pointOf(y2-1, x2)
            pto = pointOf(y1-1, x1)
            if movable(y2-1, x2, y1-1, x1, n, board) and pto not in visitdict[p1]:
                visitdict[p1].add(pto)
                visitdict[pto].add(p1)
                visitqueue.append([p1, pto, m+1])
                visitqueue.append([pto, p1, m+1])

        else:
            # pfix = p1, pmove = p2
            pvia = pointOf(y2, x2+1)
            pto = pointOf(y1, x1+1)
            if movable(y2, x2+1, y1, x1+1, n, board) and pto not in visitdict[p1]:
                visitdict[p1].add(pto)
                visitdict[pto].add(p1)
                visitqueue.append([p1, pto, m+1])
                visitqueue.append([pto, p1, m+1])

            pvia = pointOf(y2, x2-1)
            pto = pointOf(y1, x1-1)
            if movable(y2, x2-1, y1, x1-1, n, board) and pto not in visitdict[p1]:
                visitdict[p1].add(pto)
                visitdict[pto].add(p1)
                visitqueue.append([p1, pto, m+1])
                visitqueue.append([pto, p1, m+1])

    return -1

def pointOf(y, x):
    return 1000 * y + x

def xypoint(p):
    return p//1000, p%1000

def ishorizon(p1, p2):
    return p1 // 1000 == p2 // 1000

def movable(viay, viax, toy, tox, n, b):
    return -1 < viay < n and -1 < viax < n and -1 < toy < n and -1 < tox < n and b[viay][viax] == 0 and b[toy][tox] == 0