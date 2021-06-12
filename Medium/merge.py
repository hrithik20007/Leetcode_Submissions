'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''





class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=[]
        
        if len(intervals)==1:
            l.append([intervals[0][0],intervals[0][1]])
            return l

        intervals.sort(key=lambda x:x[0])                           #Sorting the list as per the first element in the sub-lists

        j=0
        for i in range(1,len(intervals)):                           #Starts iterating from the second sub-list

            if len(l)!=0 and intervals[i][0]<=l[-1][1]:             #Comapres the second element in the last sub-list in 'l' with the first element of the sub-list
                                                                    #in 'intervals', currently under consideration
                m=max(intervals[i][1],l[-1][1])
                l.append([l[-1][0],m])
                l.pop(-2)
                j+=1
            
            elif intervals[i][0]<=intervals[i-1][1]:                #Comapres the second element of the previous sub-list in 'intervals' with the first element of the
                                                                    #sub-list in 'intervals', currently under consideration
                m=max(intervals[i][1],intervals[i-1][1])
                l.append([intervals[i-1][0],m])
                j+=1
            
            else:
                if j==0:                                            #This j portion is for the first sub-list which was not iterated over. If it enters the else portion
                                                                    #in the very first iteration, that means there was no merge and we add the first sub-list to 'l'
                    l.append([intervals[0][0],intervals[0][1]])
                l.append([intervals[i][0],intervals[i][1]])         #In case of no-merge, we add the sub-list as it is, to 'l'.
                j+=1
                
        return l
        
