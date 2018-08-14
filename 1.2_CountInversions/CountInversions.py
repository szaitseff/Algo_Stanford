#-------------------------------------------------------------------------------
# Name:        CountInversions
# Purpose:     Produce number of inversions in an array of integers
#
# Author:      szaitseff
#
# Created:     22.03.2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

# Global variables
counter = 0

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno    # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
##    test(merge([4,5,6], [2,3,8,9,10]) == [2,3,4,5,6,8,9,10])
##    test(merge([],[]) == [])
##    test(merge_sort([123, 12, 3, 2, 1, 10, 15, 16]) == [1, 2, 3, 10, 12, 15, 16, 123])

    f = open("IntegerArray.txt")
    L = f.readlines()
    f.close()
    for i in range(len(L)):
        L[i] = int(L[i])
    merge_sort(L)
    print("counter =", counter)


def merge(left, right):
    result = []
    i = 0
    j = 0
    global counter    #  counts number of inversions
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            counter += len(left[i:])
    while (i < len(left)):   # when right sublist is empty
        result.append(left[i])
        i += 1
    while (j < len(right)):  # when left sublist is empty
        result.append(right[j])
        j +=1
    #print("counter =", counter)
    return result

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L)//2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)

test_suite()   # Here is the call to run the tests
