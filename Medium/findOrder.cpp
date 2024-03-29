/*
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array 
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course 
ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of 
them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]
*/






/*
Logic:
Basically we are performing a topological sort. There, the nodes with 0 indegrees are put first, then their immideate
neighbour nodes have their indegrees reduced by 1. If their indegrees become 0, they are pushed into the queue.
*/

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n=numCourses;
        vector<vector<int>> list(n,vector<int>());
        vector<int> indeg(n,0);
        vector<int> ans;
        
        int i;
        int node;
        int n1=0;
        for(i=0;i<prerequisites.size();i++){
            int u=prerequisites[i][1];
            int v=prerequisites[i][0];
            list[u].push_back(v);
            indeg[v]+=1;
        }
        
        queue<int> q;
        for(i=0;i<n;i++){
            if(indeg[i]==0)
                q.push(i);
        }
        
        while(!q.empty()){
            node=q.front();
            q.pop();
            ans.push_back(node);
            n1+=1;
            
            for(auto it:list[node]){
                indeg[it]-=1;
                if(indeg[it]==0)
                    q.push(it);
            }
        }
        
        if(n1!=n)                               //Meaning a cycle is present. So, we return an empty vector.
            return vector<int>();
        else
            return ans;
    }
};