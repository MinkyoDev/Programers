def solution(nums):
    p_dict = {}
    for num in nums:
        if num in p_dict.keys():
            p_dict[num] += 1
        else:
            p_dict[num] = 1
            
    return len(nums)//2 if len(p_dict.keys()) > len(nums)//2 else len(p_dict.keys())