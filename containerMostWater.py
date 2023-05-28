s=int(input("no of col: "))
lst1=[]
for i in range (s):
    n=int(input("level: "))
    lst1.append(n)
print(lst1)
print(len(lst1))

gap,area=0,0

for i in range(0,len(lst1)):
    for  j in range(i,len(lst1)):
        m=min(lst1[i],lst1[j])
        gap =j-i
        e=m*gap
        print("for i:",i,"for j:",j,"m=",m,"gap:",gap,"having area:",e)
        if(m*gap > area):
            area=m*gap
print(area)


