class Solution:
    """
    @param A: An integer array
    @param index1: the first index
    @param index2: the second index
    @return: nothing
    """
    def swapIntegers(self, A, index1, index2):
        # write your code here
        t = A[index1]
        A[index1] = A[index2]
        A[index2] = t
        return A
