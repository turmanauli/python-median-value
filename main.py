def findMedianSortedArrays(nums1, nums2):
        nums3 = nums1 + nums2
        rawlength = len(nums3)
        nums3.sort()
        length = math.floor(rawlength/2)
        if rawlength%2 != 0:        
            return nums3[length]
        else:
            return (nums3[length]+nums3[(length-1)])/2
