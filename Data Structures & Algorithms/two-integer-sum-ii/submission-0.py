class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        print(numbers)
        while left < right:
            if target > numbers[left]+numbers[right]:
                # print("left")
                # print(numbers[left], numbers[right])
                left+=1
            elif target < numbers[left]+numbers[right]:
                # print("right")
                # print(numbers[left], numbers[right])
                right-=1
            else:
                return [left+1,right+1]
