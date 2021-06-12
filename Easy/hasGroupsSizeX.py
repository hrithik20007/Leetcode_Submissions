'''
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:
    Each group has exactly X cards.
    All the cards in each group have the same integer.

Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
'''





#Logic: Basically I am checking for the greatest common divisor(GCD) of the element's frequencies. If it is not 1, then we will have True, otherwise False.
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c=Counter(deck)
        t=-1
        l1,l2,l3=[],[],[]
        for k,v in c.items():
            l1.append(k)
            l2.append(v)
        for i in l2:
            if i<2:
                return False
        
        j=2
        while(j<=sorted(l2)[0]):
            if l2[0]%j==0:
                l3.append(j)        #l3 stores the divisors of the smallest element's frequency.
            j+=1
            
        for i in l3[::-1]:                  #This loop checks for the greatest common divisor for element's frequencies
            for j in range(len(l2)):        
                if l2[j]%i!=0:
                    break
                if j==len(l2)-1 and l2[j]%i==0:
                    return True
                
        return False         
                
                
                
                
        '''
        c=Counter(deck)
        l=[i for i in c.keys()]
        t=c[l[0]]
        if t<2:
            return False 
        
        j=2
        while(True):       #Smallest divisor of the first element's frequency
            if t%j==0:
                break
            j+=1
            
        for i in c.keys():
            if c[i]<2:
                return False
            else:
                if c[i]!=t and c[i]%j!=0:
                    return False
                t=c[i]
        
        return True
        '''
