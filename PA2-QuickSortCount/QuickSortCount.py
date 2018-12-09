#-------------------------------------------------------------------------------
# Name:        QuickSortCount

# Signarure:   Unsorted array of integers [1, 100000] -> Integer.

# Purpose:     Compute the total number of comparisons used to sort
#              the given input by QuickSort algorithm

# Author:      szaitseff
#
# Created:     30.03.2018
# Copyright:   (c) admin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

# Global variables
counter1 = 0
counter2 = 0
counter3 = 0

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno    # Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():

##    test(QuickSort1([3,8,2,5,1,4,7,6], 0, 7) == [1,2,3,4,5,6,7,8])
##    test(QuickSort2([3,8,2,5,1,4,7,6], 0, 7) == [1,2,3,4,5,6,7,8])
##    test(QuickSort3([3,8,2,5,1,4,7,6], 0, 7) == [1,2,3,4,5,6,7,8])

    f = open("QuickSort.txt")
    A = f.readlines()
    f.close()
    for i in range(len(A)):
        A[i] = int(A[i])

    #QuickSort1(A, 0, 9999)
    #QuickSort2(A, 0, 9999)
    QuickSort3(A, 0, 9999)

    #print("counter1 =", counter1)
    #print("counter2 =", counter2)
    print("counter3 =", counter3)




def QuickSort1(A, l, r):
    """ A is an array of integers.
        l is the left-most index of subarray
        r is the right-most element of subarray
        Use the 1st element of the array as the pivot element.
    """
    global counter1    # Set up counter to compute the number of comparisons
    if (l >= r):
        return A
    else:
        # Standard Partition procedure
        p = A[l]    # use the current first element as pivot
        #print("p =", p)
        i = l       # index of the right-most item < p
        for j in range(l+1, r+1):
            if A[j] < p:
                A[j], A[i+1] = A[i+1], A[j] # swap with leftmost item > p
                i += 1
        A[l], A[i] = A[i], A[l]     # swap pivot with right-most item < p

        # Recursive sort
        counter1 += r - l
        #print("counter1 =", counter1)

        L = QuickSort1(A, l, i-1)
        R = QuickSort1(A, i+1, r)
        return A


def QuickSort2(A, l, r):
    """ A is an array of integers.
        l is the left-most index of subarray
        r is the right-most element of subarray
        Use the last element of the array as the pivot element.
    """
    global counter2    # Set up counter to compute the number of comparisons
    if (l >= r):
        return A
    else:
        # Swap the last item with 1st item
        A[l], A[r] = A[r], A[l]

        # Standard Partition procedure
        p = A[l]    # use the current 1st element as pivot
        #print("p =", p)
        i = l       # index of the right-most item < p
        for j in range(l+1, r+1):
            if A[j] < p:
                A[j], A[i+1] = A[i+1], A[j] # swap with leftmost item > p
                i += 1
        A[l], A[i] = A[i], A[l]     # swap pivot with right-most item < p

        # Recursive sort
        counter2 += r - l
        #print("counter2 =", counter2)

        L = QuickSort2(A, l, i-1)
        R = QuickSort2(A, i+1, r)
        return A


def QuickSort3(A, l, r):
    """ A is an array of integers.
        l is the left-most index of subarray
        r is the right-most element of subarray
        Use the "median-of-three"  element of the array as the pivot element.
    """
    global counter3    # Set up counter to compute the number of comparisons
    if (l >= r):
        return A
    else:
        # Find index of the "median-of-three"
        m = 0
        k = (l + r) // 2  # find index of the middle item
        if (A[k] <= A[l]) and (A[l] <= A[r]):
            m = l
        elif (A[r] <= A[l]) and (A[l] <= A[k]):
            m = l
        elif (A[l] <= A[k]) and (A[k] <= A[r]):
            m = k
        elif (A[r] <= A[k]) and (A[k] <= A[l]):
            m = k
        else:
            m = r

        A[l], A[m] = A[m], A[l]    # swap the "median-of-three" with 1st item

        # Standard Partition procedure
        p = A[l]    # use the current 1st element as pivot
        #print("p =", p)
        i = l       # index of the right-most item < p
        for j in range(l+1, r+1):
            if A[j] < p:
                A[j], A[i+1] = A[i+1], A[j] # swap with leftmost item > p
                i += 1
        A[l], A[i] = A[i], A[l]     # swap pivot with right-most item < p

        # Recursive sort
        counter3 += r - l
        #print("counter3 =", counter3)

        L = QuickSort3(A, l, i-1)
        R = QuickSort3(A, i+1, r)
        return A

test_suite()   # Here is the call to run the tests