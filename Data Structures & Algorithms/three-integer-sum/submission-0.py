class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        h=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    h.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        res=[]
        for x in h:
            res.append(x)
        return res