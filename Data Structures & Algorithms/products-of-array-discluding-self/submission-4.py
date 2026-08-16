class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        postfix_sum = []
        prefix_sum_total = 1
        postfix_sum_total = 1
        for ele in nums:
            prefix_sum_total *= ele
            prefix_sum.append(prefix_sum_total)

        for ele in nums[::-1]:
            postfix_sum_total *= ele
            postfix_sum.append(postfix_sum_total)
        postfix_sum = postfix_sum[::-1]
        res = []
        for idx in range(len(nums)):
            if idx == 0:
                prefix = 1
                post_fix = postfix_sum[idx+1]
            elif idx == len(nums)-1:
                post_fix = 1
                prefix = prefix_sum[idx-1]
            else:
                prefix = prefix_sum[idx-1]
                post_fix = postfix_sum[idx+1]
            # print(f"Prefix : {prefix}, post_fix : {post_fix}")
            res.append(prefix * post_fix)
        return res

