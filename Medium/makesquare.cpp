/*
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You 
should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:
Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
*/








/*
Logic: We divide the total sum of the array into 4 equal parts. Now every index's value of the matchsticks array is decreased from one of the four array elements 
recursively. By the time we reach the index after the last one, all the four elements should be reduced to 0. If it is not, we backtrack and redo the procedure. If 
still no match is found after all the possible combinations, we return false, otherwise true.
*/
class Solution {
public:
    bool matchstick(vector<int>& matchsticks, int idx, vector<int> t){
        if(idx>=matchsticks.size())
            return (t[0]==0 && t[1]==0 && t[2]==0 && t[3]==0);
        
        for(int j=0;j<4;j++){
            if(matchsticks[idx]>t[j])
                continue;
            t[j]-=matchsticks[idx];
            if(matchstick(matchsticks,idx+1,t))
                return true;
            t[j]+=matchsticks[idx];
        }
        
        return false;
    }
    
    bool makesquare(vector<int>& matchsticks) {
        int i,t,s=0;
        for(i=0;i<matchsticks.size();i++)
            s+=matchsticks[i];
        
        if(s%4!=0 || matchsticks.size()<4)
            return false;
        else
            t=s/4;

        vector<int> total={t,t,t,t};
        sort(matchsticks.begin(),matchsticks.end(),greater<int>());
        return matchstick(matchsticks, 0, total);
    }
};






/*
class Solution {
    //unordered_map<vector<int>,bool>mp;
public:
    bool matchstick(vector<int>& matchsticks, int idx, int c, int t, int v){
        //if(mp.count({idx,c,t}))
            //return mp[{idx,c,t}];
        if(c==3 && t==0){
            //mp[{idx,c,t}]=true;
            return true;
        }
        else if(c<3 && t==0){
            c+=1;
            t=v;
        }
        else if(t<0 || idx>=matchsticks.size()){
            //mp[{idx,c,t}]=false;    
            return false;
        }
        //cout<<c<<" "<<t<<" "<<idx<<endl;
        if(matchstick(matchsticks,idx+1,c,t-matchsticks[idx],v) || matchstick(matchsticks,idx+1,c,t,v))
            return true;
        return false;
    */
        /*
            mp[{idx,c,t}]=true;
        else
            mp[{idx,c,t}]=false;
        
        return mp[{idx,c,t}];
        
    }
    */
    /*
    bool makesquare(vector<int>& matchsticks) {
        int i,t,s=0;
        for(i=0;i<matchsticks.size();i++)
            s+=matchsticks[i];
        
        if(s%4!=0)
            return false;
        else
            t=s/4;
        //cout<<t<<endl;
        return matchstick(matchsticks, 0, 0, t,t);
    }
};
*/
