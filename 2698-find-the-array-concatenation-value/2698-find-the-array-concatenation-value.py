class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        answer = 0

        while nums:
            if len(nums) == 1:
                answer += nums[0]
                nums.pop(0)  # 첫 번째 요소 제거
            else:
                answer += int(str(nums[0]) + str(nums[-1]))
                nums.pop(0)  # 첫 번째 요소 제거
                nums.pop()  # 마지막 요소 제거
                
        return answer
