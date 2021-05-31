'''
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

Example 1:
Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:
Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:
Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
'''




class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if rec1[0]==rec1[2] or rec1[1]==rec1[3] or rec2[0]==rec2[2] or rec2[1]==rec2[3]:    #If any of the 1st and 2nd x or y coordinates are equal(i.e. same point)
            return False
        if rec2[0]>=rec1[2]:    #When the starting index of rec2 is more than the ending index of rec1 (For x)
            return False
        if rec2[2]<=rec1[0]:    #When the ening index of rec2 is less than the starting index of rec1 (For x)
            return False
        if rec2[1]>=rec1[3]:    #When the starting index of rec2 is more than the ending index of rec1 (For y)
            return False
        if rec2[3]<=rec1[1]:    #When the ending index of rec2 is less than the starting index of rec1 (For y)
            return False
        
        return True
        
        
        
        '''
        f=0
        x=[rec1[0]+1,rec1[2]-1]
        y=[rec2[1]+1,rec2[3]-1]
        
        #For X-axis
        if rec2[0]>x[0] and rec2[0]<x[1] or rec2[2]>x[0] and rec2[2]<x[1]:
            f+=1
        if rec2[0]<=x[0] and rec2[2]>=x[1]:
            f+=1
    
        #For Y-axis
        if rec2[1]>y[0] and rec2[1]<y[1] or rec2[3]>y[0] and rec2[3]<y[1]:
            f+=1    
        if rec2[1]<=y[0] and rec2[3]>=y[1]:
            f+=1
            
        #For checking
        if f==2:
            return True
        else:
            return False
        '''
