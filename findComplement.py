class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        n=bin(num)[2:]
        n1=n.replace('0','1')
        a=int(n1,2)
        return (a-num)
        '''

        #or
        #This is my solution

        
        n=list(bin(num)[2:])
        for i in range(0,len(n)):
            if n[i]=='1':
                n[i]='0'
            else:
                n[i]='1'
                
        s1="".join(n)
        return int(s1,2)
