class Solution:
    def merge(self, n1: List[int], m: int, n2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while(len(n1)>m):
            n1.pop(-1)
        for i in n2:
            n1.append(i)
        n1=n1.sort()

        