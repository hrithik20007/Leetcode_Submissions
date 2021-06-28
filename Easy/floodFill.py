'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
'''




'''
Logic: I recursively travel to the four directions of my starting position and if the value in those positions match with the value of my initial coordinate, then
I change their value to newColor.

Role of the variables:
r = For row
c = For column
f = For the original value of my initial coordinate (given by (sr,sc) which is an input)
d = For storing the coordinates I have already traversed, otherwise it can retrace the path and an infinte loop may occur
i = During my first recursive function call, d will have my initial coordinates, but I cannot return from the function. I may do so, in the later calls.
    'i' keeps track whether it is my first call or not.
'''

class Solution(object):
    
    def recursive(self,r,c,image,newColor,f,d,i):   
        if r==-1 or r==len(image) or c==-1 or c==len(image[0]): 
            return
        else:
            if i!=0:
                if (r,c) in d:
                    return
            if image[r][c]==f:
                image[r][c]=newColor
            else:
                return
        
        i+=1
        d.append((r,c))
        self.recursive(r+1,c,image,newColor,f,d,i)
        self.recursive(r-1,c,image,newColor,f,d,i)
        self.recursive(r,c+1,image,newColor,f,d,i)
        self.recursive(r,c-1,image,newColor,f,d,i)
        return
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        d=[]
        d.append((sr,sc))
        i=0
        f=image[sr][sc]
        self.recursive(sr,sc,image,newColor,f,d,i)
        image[sr][sc]=newColor
        return image
