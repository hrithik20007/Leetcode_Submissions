'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Returns the necessary strings if the list is blank or contains only one word
        if(len(strs)==0):
            return ""
        elif(len(strs)==1):
            return strs[0]
        
        else:
            i=strs[0]
            l=len(i)
            
            #Stores the longest common string in the first iteration as i and then compares that with the next iterations to get longest common prefix string
            for j in strs[1:]:
                while(i!=j[0:l]):
                    i=i[0:l-1]
                    l=l-1
                    
                    if l==0:
                        return ""
            return i
        '''
        p=0
        f=""
        if(len(strs)==0):
            return ""
        elif(len(strs)==1):
            return strs[0]
        else:
            i=strs[0]
            l1=len(strs)
            l2=len(i)
            l=1
            while(l<l2):
                if(f==""):
                    x=i[0:l]
                    l=l+1
                    for j in strs[1:]:
                        a=j.split(x)
                        if len(a)>1:
                            p=p+1
                            if(p!=l1-1):
                                f=x[0:l-2]
                else:
                    break

            return f
        '''
