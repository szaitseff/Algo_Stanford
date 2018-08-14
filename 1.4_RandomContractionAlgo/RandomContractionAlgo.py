#-------------------------------------------------------------------------------
# Name:        Random contraction algorithm (aka Karger algorithm)
# Purpose:     Programming Assignment 3 at Stanford "Algorithms P1" @Lagunita
#
# Author:      szaitseff
#
# Created:     05.04.2018
# Copyright:   (c) szaitseff 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys
import copy
import random
rng = random.Random()

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno    # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
##    L = readAdjList("kargerMinCut.txt")
##    print(L)
##    test(replace([[3,8,2],[2,5,3],[1,4,2],[7,6,2]], 3, 2) == [[3,8,3],[3,5,3],[1,4,3],[7,6,3]])
##    test(removeSelfLoops([2,5,2,3,2,8,2,10,2,2,2]) == [2,5,3,8,10])
##    m = kargerAlgo(L)
##    print("m =", m)

    minCut = repetitiveRun("kargerMinCut.txt", 100)
    print("minCut =", minCut)


def repetitiveRun(filename, N):
    """Run Karger's algorithm N = n^2*ln(n) times"""
    L = readAdjList(filename)
    C = copy.deepcopy(L)
    minCut = kargerAlgo(C)
    for i in range(N):
        C = copy.deepcopy(L)
        m = kargerAlgo(C)
        if m < minCut:
            minCut = m
    return minCut

def kargerAlgo(L):
    """Random contraction alforithm by Karger - returns cut represented
        by the final 2 vertices.
    """
    if len(L) < 2:
        return 0
    else:
        while len(L) > 2:
            # pick an edge uniformly at random
            i = rng.randrange(len(L))       # random index of a row
            u = L[i][0]                     # the 1st vertex
            j = rng.randrange(1, len(L[i])) # random index of item in the row
            v = L[i][j]                     # the 2nd vertex

            # merge (or "contract") u and v into a single vertex u
            k = 0
            while k < len(L):
                if L[k][0] == v:
                    L[i] += L[k]
                    d = k
                    break
                k += 1
            # replace all references to v by u
            L = replace(L, u, v)
            # remove self-loops
            L[i] = removeSelfLoops(L[i])
            # delete 2nd vertex
            del L[d]

        # return number of edges between the final 2 vertices
        m = len(L[0]) - 1
        return m

def readAdjList(filename):
    """ read the adjacency list (nested, with rows as inner lists) """
    f = open(filename)
    L = f.readlines()
    f.close()
    for i in range(len(L)):
        L[i] = L[i].split()
        for j in range(len(L[i])):
            L[i][j] = int(L[i][j])
    return L

def replace(L, x, y):
    """ replaces items y by items x in a nested list. """
    for i in range(len(L)):
        for j in range (len(L[i])):
            if L[i][j] == y:
                L[i][j] = x
    return L

def removeSelfLoops(L):
    """ removes items equal to 1st item in a list. """
    t = len(L)
    i = 1
    while i < t:
        if L[i] == L[0]:
            del L[i]
            t -= 1
        else:
            i += 1
    return L


test_suite()   # Here is the call to run the tests



