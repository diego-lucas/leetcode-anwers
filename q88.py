class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        
        nums1_c = nums1[:m]
        total = len(nums1_c) + len(nums2)

        cont = 0
        final = []

        while (cont < total):
            if len(nums1_c) == 0:
                final.append(nums2[0])
                del nums2[0]
            elif len(nums2) == 0:
                final.append(nums1_c[0])
                del nums1_c[0]
            else:
                if nums1_c[0] < nums2[0]:
                    final.append(nums1_c[0])
                    del nums1_c[0]
                else:
                    final.append(nums2[0])
                    del nums2[0]
            
            cont += 1
        for i in range(len(nums1)):
            del nums1[0]
        for i in final:
            nums1.append(i)
