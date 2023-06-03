
"""
for  n=5:  
    1 2 3 4 5
    11 12 13 14 15
    21 22 23 24 25
    16 17 18 19 20
    6 7 8 9 10
for n=4:
    1 2 3 4 
    9 10 11 12 
    13 14 15 16
    5 6 7 8 

"""


n=int(input())
#list of list
"""
[[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
"""
a=[[0 for i in range(n)]
  for i in range(n)]
up=0
down=n-1
l=0
while up<down:
  for j in range(0,n):
    l=l+1
    #print("up:",up,";j",j)
    a[up][j]=l
  for j in range(0,n):
    l=l+1
    #print("down:",down,";j",j)
    a[down][j]=l
  up=up+1
  down=down-1
if(up==down):
  for j in range(0,n):
    l=l+1
    #print("down:",down,";j",j)
    a[down][j]=l
print("afteriti, up: ",up,'down:',down,'l=  ',l)
for i in range(n):
        for j in range(n):
            print(a[i][j], end = '')
        print()
        

#print(a)
