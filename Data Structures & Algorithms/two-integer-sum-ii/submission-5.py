class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right = len(numbers) - 1
        left = 0
        while numbers[right] + numbers[left] != target:
            if numbers[right] + numbers[left] < target:
                left += 1
            elif numbers[right] + numbers[left] > target:
                right -= 1
        return [left + 1, right + 1]
        