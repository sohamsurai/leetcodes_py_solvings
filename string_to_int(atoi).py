 #s=input("string: ")
        #print("ip",s)
        op=0
        start=0
        sign=1
        maxI=(2**31)-1
        minI =-2 **31
        result=0
        s=s.lstrip()
        if not s:return result
        #print("strip",s)
        
        if (s[start]=='-'):
            sign =-1 
            start=start+1
        elif(s[start]=='+'):
            sign=1
            start=start+1
        #print("start:",start)
       # if(start !=len(s)):
        #    while (s[start]==0):
         #       start=start+1

        #print("start:",start)
        #print("op",op)
        for i in range (start,len(s)):
            if s[i].isdigit():
                #print("digit:",s[i])
                op=(op*10)+(int(s[i]))
                #print("op",op)
            else:
                break

        if op*sign >maxI:
            return maxI
        elif op*sign <=minI:
            return minI
        else:
            return op*sign

