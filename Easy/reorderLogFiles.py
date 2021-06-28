'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
    Letter-logs: All words (except the identifier) consist of lowercase English letters.
    Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
    The letter-logs come before all digit-logs.
    The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
    The digit-logs maintain their relative ordering.
Return the final order of the logs.

Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''






class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d={}                                #Maps the second half of alphabets (which acts as the key) with their identifiers (We store the identifiers as 
                                            # the values of the dictionary as lists. In case of similar keys (i.e. similar second half of alphabetical logs, we
                                            #append the identifiers of the same key, to the value. Later we sort the values of similar key)).
        dig=[]                              #Stores the digit logs (the entire log)
        let=[]                              #Stores the second half the alphabetical logs
        l=[]                                #Stores the answer list
        
        for i in logs:
            s1=i.split(" ",1)
            
            if s1[1][0].isdigit():
                dig.append(" ".join(s1))
                
            elif s1[1][0].isalpha():
                if s1[1] not in d:
                    d[s1[1]]=[s1[0]]
                else:
                    d[s1[1]]+=[s1[0]]
                let.append(s1[1])
                
        let.sort()                          #Sorts the second half of the alphabetical logs

        for i in let:
            if len(d[i])>1:                 #In cases of similar second half logs, the identifiers are in a list. We take smallest identifier first.
                d[i].sort()
                n=d[i].pop(0)
            else:
                n=d[i][0]                   #In cases of unique second half of the logs
            l.append(n+" "+i)
            
        for i in dig:                       #The digit logs are added at last in the order as they initially were in the given list
            l.append(i)
            
        return l
        
        
        
        
        '''
        This solution also works but the above solution is more simplified
        

        
        d={}
        dig=[]
        let=[]
        l=[]
        for i in logs:
            s1=i.split(" ",1)
            
            if s1[1][0].isdigit():
                if s1[0] not in d:
                    d[s1[0]]=[s1[1]]
                else:
                    d[s1[0]]+=[s1[1]]
                dig.append(s1[0])
                
            elif s1[1][0].isalpha():
                if s1[1] not in d:
                    d[s1[1]]=[s1[0]]
                else:
                    d[s1[1]]+=[s1[0]]
                let.append(s1[1])
                
        let.sort()
        for i in let:
            if len(d[i])>1:
                d[i].sort()
                n=d[i].pop(0)
            else:
                n=d[i][0]
            l.append(n+" "+i)
            
        for i in dig:
            if len(d[i])>1:
                n=d[i].pop(0)
            else:
                n=d[i][0]
            l.append(i+" "+n)
            
        return l
        '''
