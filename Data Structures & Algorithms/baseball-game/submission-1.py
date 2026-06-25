class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        answer = 0
        for operation in operations:
            print(nums)
            if isInt(operation):
                nums.append(operation)
            elif operation == '+':
                length = len(nums)
                nums.append(int(nums[length - 1]) + int(nums[length - 2]))
            elif operation == 'D':
                length = len(nums)
                nums.append(int(nums[length - 1]) * 2)
            elif operation == 'C':
                nums.pop()
        for num in nums:
            answer += int(num)
        return answer

def isInt(val):
        try:
            int(val)
            return True
        except ValueError:
            return False