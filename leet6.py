class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leng = len(nums)
        left_product = [1]*leng
        right_product = [1]*leng
        result = [1] * leng

        #calculate product of each value on the left
        for i in range(1,leng):
            left_product[i] = left_product[i-1] * nums[i-1]
        #right product of each element
        for i in range(leng-2,-1,-1):
            right_product[i] = right_product[i+1] * nums[i+1]

         #result is product fo right_product and left_product
        for i in range(leng):

            result[i] = right_product[i] * left_product[i]   

        return result   
        
