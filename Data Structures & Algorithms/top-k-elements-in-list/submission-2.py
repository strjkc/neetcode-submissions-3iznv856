class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = {}
        for num in nums:
            if num not in items:
                items[num] = 1
            else:
                items[num] += 1
        arr = [[] for i in range(len(nums) + 1)]
        for key, value in items.items():
            arr[value].append(key)
        fin = []
        for i in range(len(arr)-1, 0, -1):
            for num in arr[i]:
                fin.append(num)
                if len(fin) == k:
                    return fin
        