'''
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the 
past 3000 milliseconds (including the new request). 
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input:
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]                        #Keep in mind these times are send individually as t (not as a list as shown here).
Output
[null, 1, 2, 3, 3]                                      #Returns individually, not in a list

Explanation:
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
'''




class RecentCounter:

    def __init__(self):                 #As it is given RecentCounter() initializes counter with zero recent requests, we use an __init__ (constructor) function to
                                        #do the job by default.
        self.counter=[]

    def ping(self, t: int) -> int:
        r=[t-3000,t]                    #r stores the range in which we have to check our 't's. As the new t will be equal to the higher range, it will always be in
                                        #range. We are mainly concerned with the lower 't's, which may not remain in range r, when t gets higher.
        self.counter.append(t)
        while self.counter[0]<r[0]:
            self.counter.pop(0)         #Pops the beginning elements which come out of the lower range.
        return len(self.counter)        #Returns the length of the final list


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
