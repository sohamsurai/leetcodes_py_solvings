import math
x=int(input("integer"))
#assert pow(-2,31)<n <= pow(2,31) - 1,"WRONG INPUT"
max= (2 ** 31)-1
min= (-2)**31

rev=0

while x:
    d=int(math.fmod(x,10))
    print("singe char: ",d)
    #rev=rev*10+d
    x=int(x/10)
    print("remaining",x)
    if rev>max//10 or (rev==max//10 and d>=max%10):
        print(0)
    if rev<min//10 or (rev==min//10 and d<=min%10):
        print(0)
    rev=rev*10+d
print(rev)
