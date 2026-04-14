class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items = {}
        for num in nums:
            if num not in items:
                items[num] = 1
            else:
                items[num] += 1

        arr = []
        for i in range (k):
            key = max(items, key=items.get)
            arr.append(key)
            del items[key]
        return arr