class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        """
        We need to go through each of the slots up until we have no more slots to compare
        use two pointer method? Cannot just iterate though the slots
        """
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        s1 = 0
        s2 = 0
        # we would want to update the pointers if the range for the slot is greater than the other
        # id slot 1 has a lower range than slot2 advance slot 1
        while s1 < len(slots1) and s2 < len(slots2):
            start = max(slots1[s1][0], slots2[s2][0])
            end = min(slots1[s1][1], slots2[s2][1])
            if end - start >= duration:
                return [start, start+duration]
            
            if slots1[s1][1] < slots2[s2][1]:
                s1 += 1
            else:
                s2 += 1
        
        return []