'''
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:
abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted 
while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
Return the number of columns that you will delete.
'''





lass Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        m=len(strs)
        n=len(strs[0])
        c=0
    
        for i in range(n):                      #Column loop
            for j in range(1,m):                #Row loop starting from index 1
                if strs[j][i]<strs[j-1][i]:     #Checking whether in lexicographical order
                    c+=1
                    break
                
        return c
    
        
        
        
        '''
        This works but I wanted a faster solution
        
        
        m=len(strs)
        n=len(strs[0])
        a=[]
        c=0
    
        for i in range(n):
            for j in range(m):
                a.append(strs[j][i])
            if a!=sorted(a):
                c+=1
            a=[]
                
        return c
        '''
