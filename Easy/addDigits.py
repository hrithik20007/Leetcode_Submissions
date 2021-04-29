class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=[] #Stores the sums of digits after each complete iteration
        if len(str(num))==1:
            return num
        else:
            while(num>9): #The loop runs as long as there are two or more digits in the number
                s1=sum([int(i) for i in str(num)])  #sum() adds the numbers in a list. Here, a list of digits is formed, which is then summed.
                if s1 in s:
                    return False  #If a sum repeats, that means a loop has formed and the number of additions will become infinity
                if s1 not in s:
                    s.append(sum)
                num=s1
            return s1    
            
        '''
        Time limit exceeded
        
        if num==0:
            return 0
        else:
            s=0
            while(num>0):
                for i in str(num):
                    s=s+int(i)
                num=s
                
            return num
        '''
