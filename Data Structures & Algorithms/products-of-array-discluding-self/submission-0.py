class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            nums_copy = nums.copy()
            nums_copy[i] = nums_copy[-1]
            nums_copy.pop()
            product = nums_copy[0]
            for i in range(1, len(nums_copy)):
                product = product * nums_copy[i]
            products.append(product)
        
        print(products)
        return products