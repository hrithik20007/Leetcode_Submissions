'''
There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.

Example 1:
Input: moves = "UD"
Output: true
Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

Example 2:
Input: moves = "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
'''



class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        #Logic of both the solutions is that the no. of U should be equal to D and same for L and R.
        
        x=0
        y=0
        for i in moves:
            if i=="U":
                x+=1
            if i=="D":
                x-=1
            if i=="R":
                y+=1
            if i=="L":
                y-=1
            
        return x==y==0
        '''
        This is my solution but the above solution is slightly faster
        
        
        c=Counter(moves)
        if c["U"]==c["D"] and c["L"]==c["R"]:
            return True
        else:
            return False
        '''
