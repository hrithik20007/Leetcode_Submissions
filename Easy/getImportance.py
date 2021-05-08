'''
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.
For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
'''



"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    
    def recursive(self,dic,id):
        employee=dic[id]
        for j in employee.subordinates:     #For each subordinate of the original id (at first, before recursion starts. After which the id becomes the ids of the subordinates inside the subordinates list).
            employee.importance+=self.recursive(dic,j)   #Recursively goes inside every subordinates' subordinates list.
        return employee.importance      #It will return after it encounters an empty subordinate list
    
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        dic={}
        for i in employees:
            dic[i.id]=i     #dic becomes a dictionary with employee ids as the keys and each sublist within employees as the consecutive values.
            
        return self.recursive(dic,id)
        
        
        
        
        '''
        #employees=sorted(employees, key=itemgetter(0)) (Dosent work as 'Employee' object does not support indexing)
        l1=[]
        for i in range(0,len(employees)):
            if id==employees[i].id:
                p=i
                break
                
        l1.append(employees[p].importance)
        l2=employees[p].subordinates[:]
        for j in range(0,len(employees)):
            if employees[j].id in l2:
                l2=l2+(employees[j].subordinates)
                l1.append(employees[j].importance)
        
        if len(l1)==len(l2):
            for k in range(0,len(employees)):
                if employees[k].id==l2[-1]:
                    q=k
                    break
            
            l1.append(employees[q].importance)
        
        return sum(l1)
        '''
