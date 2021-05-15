class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2 or len(s)==len(list(set(list(s)))):
            return len(s)
        l1=[]
        j=0
        m=0
        while (j<len(s)):
            if s[j] not in l1:
                l1.append(s[j])    #Adds non-repeating characters
                m=max(m,len(l1))    #For storing maximum length
                j+=1
            else:
                l1=l1[1:]   #Deletes the first element until there is no repeating element (as in this case j does not increase)
        return m
        '''
        This is my solution but I wanted a faster one 
        
        
        l1=[]
        l2=[]
        if len(s)==1 or len(s)==0 or len(s)==len(list(set(list(s)))):
            return len(s)
        for i in range(0,len(s)):
            if s[i] not in l1:
                l1.append(s[i])
            else:
                l2.append(len(l1))
                l1=[]
                j=i-1
                while(s[i]!=s[j]):  #Retraces back to the last point of occurence of the current element under consideration
                    j-=1
                for k in range(j+1,i+1):
                    l1.append(s[k])     #l1 is updated to the form where the last occured element is deleted
                
        l2.append(len(l1))  #For adding the length of the last string with non-repeating elements (after the for loop ends).
        return max(l2)
        '''
