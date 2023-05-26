class Solution:
    def longestPalindrome(self, s: str) -> str:
        result =""
        reslen=0
        for i in range(len(s)):
            result,reslen=check_pallindrome(i,i,s,result,reslen)
            result,reslen=check_pallindrome(i,i+1,s,result,reslen)
        return result
    
def check_pallindrome(left,right,str,res,reslen):
    
    while(left>=0 and right<len(str) and str[left]==str[right]):
        #result1=str[left:right+1]
        if(right-left+1)>reslen:
            res=str[left:right+1]
            reslen=right-left+1
            
        left-=1
        right+=1
        
    return res,reslen