class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[1]*n
        suf=[1]*n

        pro=1
        for i in range(n):
            pre[i]=pro
            pro=pro*nums[i]
        
        pro=1
        for i in range(n-1,-1,-1):
            suf[i]=pro
            pro=pro*nums[i]

        for i in range(n):
            nums[i]=pre[i]*suf[i]
        return nums
