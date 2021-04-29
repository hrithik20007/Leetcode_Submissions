#Changing a given roman string to an integer number

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)-1
        t=0
        for i in range(0,l):
            if a.get(s[i])<a.get(s[i+1]):
                t=t-a.get(s[i])
            else:
                t=t+a.get(s[i])
                
        total=t+a.get(s[l-1])
        return total


'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        freq={}
        c={}
        
        #To calculate the frequency of characters in the dictionary
        for i in s:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
                
        #To check for similiar keys
        for j in freq:
            if j in a:
                c1=freq[j]*a[j]
                c[j]=c1
            else:
                continue
             
        #To store the index of all the roman values    
        m=s.find('I')
        n=s.find('V')
        o=s.find('X')
        p=s.find('L')
        q=s.find('C')
        r=s.find('D')
        s=s.find('M')
            
        #To store the indexes as dictionary with the romn values as key    
        z={'I':m,'V':n,'X':o,'L':p,'C':q,'D':r,'M':s}
        for key in dict(z):
            if z[key]==-1:
                z.pop(key, None)
               
        #To store the position in case a lower roman value comes before a higher one 
        h=0
        y=z['I']
        for x in z:
            if z[x]<y:
                y=z[x]
            else:
                h=x
                break
                
        t=0
        #Calculating the total    
        if h==0:
            for r in c:
                t=t+c[r]
        else:
            for r in c:
                t=t+c[r]
            t=t-2*c[h]
            
        print(t)
'''
