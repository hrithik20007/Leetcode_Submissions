'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]

Example 3:
Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]
'''





class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        r=[]
        d1={}
        d2={}
        for i,k in enumerate(list1):    #enumerate() takes a list and forms a tuple with index(starting from 0) as first element and the list characters as the 
                                        #second element. Here, i represents index while k, the characters from the list. We can provide a no. as the second
                                        #parameter in enumerate() in which case, the indexing will start from that number.
            d1[k]=i     #d1 has list characters as keys and their index as values
        for i1,k1 in enumerate(list2):
            if k1 in list1:
                d2[k1]=i1+d1[k1]    #d2 has common characters from both the lists as keys and the sum of their indexes as values
                
        n=min(j for j in d2.values())   #Minimum index sum
        
        for p in d2.keys():
            if n==d2[p]: 
                r.append(p)  #Appends characters with minimum sum
        
        return r


        #The following 2 are my solutions but I wanted a faster solution.

        
        '''
        l=[]
        r=[]
        c=[]
        for i in list1:
            if i in list2:
                l.append(i)
                
        for j in l:
            s=list1.index(j)+list2.index(j)
            c.append(s)
        n1=min(c)
                
        for k in l:
            if list1.index(k)+list2.index(k)==n1: 
                r.append(k)
        
        return r
        '''


        '''
        l=[]
        l1=[]
        l1.append("xyz")
        c=sys.maxsize
        f=0
        for i in list1:
            if i in list2:
                l.append(i)
                
        for j in l:
            s=list1.index(j)+list2.index(j)
            
            if c!=s:
                f+=1
            if c>s:
                c=s
                l1[0]=j
                
        if f==1:
            return l
        else:
            return l1
        '''
