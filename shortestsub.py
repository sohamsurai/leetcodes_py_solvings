nums = input().split()
lst=[]
print(nums)
print(type(nums))
for i in range (0,len(nums)-1):
        if ((nums[i+1]<nums[i])):
           lst.append(i)
print (lst)
if (len(lst)>1):
    print ((len(lst)+lst[0])+1)
elif(len(lst)==0):
    print (0)
else: 
    print (2)
        


