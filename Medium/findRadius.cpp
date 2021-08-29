/*
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.
Every house can be warmed, as long as the house is within the heater's warm radius range. 
Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.
Notice that all the heaters follow your radius standard, and the warm radius will the same.

Example 1:
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Example 3:
Input: houses = [1,5], heaters = [2]
Output: 3
*/






/*
Logic: We are basically finding the largest distance between any house and its closer heater(either from the left or right). We do this via binary search.
*/
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(heaters.begin(),heaters.end());
        sort(houses.begin(),houses.end());
        
        long long int i,j,l=0,r=INT_MAX,res=-1,mid;
        while(l<=r){
            mid=(l+r)/2;
            j=0;
            for(i=0;i<heaters.size();i++){
                while(j<houses.size() && abs(houses[j]-heaters[i])<=mid)
                    j+=1;
            }
            
            if(j==houses.size()){
                res=mid;
                r=mid-1;
            }
            else
                l=mid+1;
        }
        
        return res;
    }
};






/*
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(heaters.begin(),heaters.end());
        
        int i,dist=0,ans=0;
        for(i=0;i<houses.size();i++){
            //cout<<i<<endl;
            int j1=0,j2=1;
            if(houses[i]<heaters[0])
                dist=heaters[0]-houses[i];
            else if(houses[i]>heaters[heaters.size()-1])
                dist=houses[i]-heaters[heaters.size()-1];
            else{
                while(houses[i]!=heaters[j1] && houses[i]!=heaters[j2] && heaters[j1]<houses[i] && houses[i]>heaters[j2]){
                    j1+=1;
                    j2+=1;
                }
                //cout<<j1<<j2<<endl;
                if(houses[i]==heaters[j1] || houses[i]==heaters[j2])
                    dist=0;
                else
                    dist=min(houses[i]-heaters[j1],heaters[j2]-houses[i]);
                //cout<<"Dist : "<<dist<<endl;
            }
            
            ans=max(ans,dist);
        }
        
        return ans;
    }
};
*/
