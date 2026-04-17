class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        i=0
        h={}
        for x in nums:
            if target-x in h.keys():
                ans.append(h[target-x])
                ans.append(i)
            else:
                h[x]=i
            i+=1
        return ans