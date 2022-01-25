/*
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports 
of one flight. Reconstruct the itinerary in order and return it.
All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are 
multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single 
string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
*/







/*
Logic: (Watch Tech Dose for better explaination)
We create an adjacency list using a map of multiset (similar to set but allows multiple similar values). As we are asked
to return the vector in lexicographical order, we use a multiset as it already stores the strings in a sorted manner, so 
when we traverse over them, the strings pushed into the answer vector are also in lexicographical order. We also use a set.
We do so as when we traverse the graph, it may happen that we reach a dead end without traversing all the airports. By
implementing a stack, if we encounter such an airport which dosen't have an adjacent airport, we pop it out of the stack
and push it into our answer. (Actually, we should have eventually reached this aiport at the end, however due to the
ordering of the multiset, we have reached it before than necessary). Also, if we have covered an aiport, we erase it from 
the current airport's multiset. Finally, the answer that we get is in reverse order. So we reverse it again.
*/

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        map<string,multiset<string>> list;
        vector<string> ans;
        stack<string> s;
        
        int i;
        for(i=0;i<tickets.size();i++)
            list[tickets[i][0]].insert(tickets[i][1]);
        
        s.push("JFK");
        while(!s.empty()){
            string node=s.top();
            if(list[node].size()==0){
                ans.push_back(node);
                s.pop();
            }
            else{
                auto it=list[node].begin();
                s.push(*it);
                list[node].erase(it);            
            }
        }
        
        reverse(ans.begin(),ans.end());
        return ans;
    
        
    /*
    Gives TLE
    
    
    
    int set_size=0;
    void dfs(string node,map<string,vector<string>> list,map<pair<string,string>,int> &vis,vector<vector<string>> &res,vector<string> l,set<string> s){
        s.insert(node);
        l.push_back(node);
        if(list[node].size()==0){
            if(s.size()==set_size)
                res.push_back(l);
            return;
        }
        
        int c=0;
        for(auto it:list[node]){
            if(vis[{node,it}]!=0){
                c+=1;
                vis[{node,it}]-=1;
                dfs(it,list,vis,res,l,s);
                vis[{node,it}]+=1;
            }
        }
        
        if(c==0 && s.size()==set_size)
            res.push_back(l);
        return;
    }
    
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        map<string,vector<string>> list;
        map<pair<string,string>,int> vis;
        vector<vector<string>> res;
        set<string> s;
        
        int i;
        for(i=0;i<tickets.size();i++){
            s.insert(tickets[i][0]);
            s.insert(tickets[i][1]);
            vis[{tickets[i][0],tickets[i][1]}]+=1;;
            list[tickets[i][0]].push_back(tickets[i][1]);
        }
    
        set_size=s.size();
        s.clear();
        dfs("JFK",list,vis,res,vector<string>(),s);
        
        sort(res.begin(),res.end());
        return res[0];
    */
    }
};