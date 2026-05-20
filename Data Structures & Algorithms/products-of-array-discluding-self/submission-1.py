class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            pre, suf = nums[:i], nums[i + 1:]
            product = pre[0] if pre else suf[0]
            pre_range = range(1, len(pre)) if len(pre) > 0 else []
            suf_range = range(len(suf)) if len(pre) else range(1, len(suf))
            for n in pre_range:
                product = product * pre[n]
            for x in suf_range:
                product = product * suf[x]
            products.append(product)
        
        
        print(products)
        return products