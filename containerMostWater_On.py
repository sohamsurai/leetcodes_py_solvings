s=int(input("no of col: "))
lst1=[]
for i in range (s):
    n=int(input("level: "))
    lst1.append(n)
print(lst1)
print(len(lst1))
maxArea=0
left=0
right=len(lst1)-1

while left<right:
    maxArea=max(maxArea,(right-left)*min(lst1[left],lst1[right]))
    if lst1[left]<lst1[right]:
        left=left+1
    elif lst1[left]>lst1[right]:
        right=right-1
    else:
        left=left+1
print(maxArea)
    