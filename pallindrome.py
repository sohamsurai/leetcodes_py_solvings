     n=input()
     n=x
     rev =0
     while(x):
        op=int(x%10)
        x=int(x/10)
        rev=(rev*10)+op
        if (n==rev):
            return True
        else:
            return False