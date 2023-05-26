nums =[-2,1,-3,4,-1,2,1,-5,4]
nums =[-2,1,-3,4,-1,2,1,-5,4]
max_sum,cur_sum=0,-inf
for i in nums:
    cur_sum = max(i,cur_sum)
    max_sum = max(cur_sum,max_sum)
rprint(max_sum)