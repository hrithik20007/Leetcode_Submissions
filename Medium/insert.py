'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''





#Logic: Same as merge.py but with one extra step of inserting a sub-list
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l=[]
        intervals.append(newInterval)                               #Inserts the new sub-list to the given list
        intervals.sort(key=lambda x:x[0])                           #Sorting the list as per the first element in the sub-lists
        
        if len(intervals)==1:
            l.append([intervals[0][0],intervals[0][1]])
            return l

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
