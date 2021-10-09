/*
Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:
    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
*/





/*
Logic: A vector is globally initialised. When the constructor is called, then we declare its values and length.
Note - We don't say "vector<bool> v(1000001,false)", as it will re-initialise the vector and this time non-
globally. So we do "v=vector<bool>(1000001,false)". When a key is added, we make the key's index true and vice-
versa while removal. While checking, we simply check whether the index element is true or false.
*/
class MyHashSet {
public:
    vector<bool> v;
    MyHashSet() {
        v=vector<bool>(1000001,false);
    }
    
    void add(int key) {
        v[key]=true;
    }
    
    void remove(int key) {
        v[key]=false;
    }
    
    bool contains(int key) {
        return v[key]==true;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */