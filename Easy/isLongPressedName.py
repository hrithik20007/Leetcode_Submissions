'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
'''





class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a=list(name)
        b=list(typed)
        if len(a)>len(b):
            return False
        last=None

        while(len(a)>0 and len(b)>0):
            if a[0]==b[0]:              #Pops first element from both the lists if same and keeps track of the last element of a 
                last=a.pop(0)
                b.pop(0)
            else:
                if b[0]!=last:          #If the last element does not match with b's latest element, then returns False , otherwise b's first element
                    return False
                else:
                    b.pop(0)
            
        while(len(b)>0):                #After while loop ends, b may still have elements. It is okay as long as b's last elements match with a's last element
            if last==b[0]:
                b.pop(0)
            else:
                return False
        
        if len(a)==0:                   #After all the code, it may still happen that 'a' has some odd elements left at the end. Then it will return False
            return True
        else:
            return False
        


        
        '''
        j=0
        for i in range(len(name)):
            if name[i]!=typed[j]:
                    return False
            
            if i!=len(name)-1 and name[i]==name[i+1]:
                j+=1
                continue
            
            f=0
            while(j+1<len(typed) and name[i]==typed[j+1]):
                j+=1
                f=1
            
            if f==1:
                j-=1
            else:
                j+=1
        
        return True
        '''
    


    
        '''
        c1={}
        c2={}
        for i in name:
            if i in c1:
                c1[i]+=1
            else:
                c1[i]=1
        for i in typed:
            if i in c2:
                c2[i]+=1
            else:
                c2[i]=1
        l1,l2=[],[]
        l1=[i for i in c1.keys()]
        l2=[i for i in c2.keys()]
        if len(l1)!=len(l2):
            return False
        for i in range(len(l1)):
            if l1[i]!=l2[i]:
                return False

        for i in c2.keys():
            if c2[i]<c1[i]:
                return False
        return True
        '''
