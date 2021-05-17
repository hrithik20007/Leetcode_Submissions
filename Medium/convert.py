'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
'''





class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or len(s)==numRows:
            return s
        st=""
        l=[[] for i in range(numRows)]
        n1=numRows+(numRows-2)  #No. of elements in (numRows-1) columns before the zigzag pattern repeats
        n2=len(s)//n1
        n3=(n2+1)*(numRows-1)   #Total no. of columns of the 2d list
        for i in range(numRows):
            l[i]=[0]*n3     #Initialising the 2d list
        a=0 #For row no.
        b=0 #For column no.
        f=0

        for j in s:
            if f==0 and a<numRows:  #This if statement is for when the characters continue downwards in the same column
                l[a][b]=j
                a+=1
                if a==numRows:
                    f=1
                    a-=1    #Becuase a's value is currently numRows
                    continue    #If we don't write continue, then it will enter the second if statement with the same character and it will have an extra unnecessary repeat
            if f==1:    #This if statement is for when the characters move diagonally upwards towards the right
                a-=1
                b+=1
                if a==0:    #Only for the case where numRows=2
                    f=0
                    l[a][b]=j
                    a+=1
                if f==1:
                    l[a][b]=j
                    if a==1:    #That is, a has reached the second row, after which it must go to the first if statement
                        a=0
                        b+=1
                        f=0

        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]!=0:
                    st=st+str(l[i][j])

        return st
