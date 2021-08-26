/*
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.
A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are 
valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.
A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
    1 <= xi.length <= 4
    xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
    Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and 
"02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

Example 1:
Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Example 4:
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"

Example 5:
Input: IP = "1e1.4.5.6"
Output: "Neither"
*/









/*
Logic: In the validIPAddress function, we have divided the string into sections of string separated by '.' or ':' and put them into a string vector 'l'. After that
we check whether the sections of string produce valid IP addresses. We send the vector to 'ipv4' function if the strings are separated by '.', else we send it to 
'ipv6' function to check whether they are valid.
*/
class Solution {
public:
    string ipv4(vector<string> &l){
        int i,j,x;
        if(l.size()!=4)
            return "Neither";
        for(i=0;i<l.size();i++){
            if(l[i].length()>3 || l[i].length()==0)
                return "Neither";
            else if(l[i].length()>1 && l[i][0]=='0')
                return "Neither";
            for(j=0;j<l[i].length();j++){
                if(isdigit(l[i][j]))
                    continue;
                else
                    return "Neither";
            }
            
            x=stoi(l[i]);
            if(x>255 || x<0)
                return "Neither";
        }
        
        return "IPv4";
    }

    
    string ipv6(vector<string> &l){
        int i,j;
        if(l.size()!=8)
            return "Neither";
        for(i=0;i<l.size();i++){
            if(l[i].length()>4 || l[i].length()==0)
                return "Neither";
            for(j=0;j<l[i].length();j++){
                if(isdigit(l[i][j]) || l[i][j]=='a' || l[i][j]=='b' || l[i][j]=='c' || l[i][j]=='d' || l[i][j]=='e' || l[i][j]=='f' || l[i][j]=='A' || l[i][j]=='B' || l[i][j]=='C' || l[i][j]=='D' || l[i][j]=='E' || l[i][j]=='F')
                    continue;
                else
                    return "Neither";
            }
        }
        
        return "IPv6";
    }


    
    string validIPAddress(string IP) {
        int i,f=0,c=0;
        string s1="";
        vector<string> l;
        for(i=0;i<IP.length();i++){
            if(f==0 && IP[i]=='.'){
                f=1;
                l.push_back(s1);
                s1="";
                c=1;
            }
            else if(f==0 && IP[i]==':'){
                f=2;
                l.push_back(s1);
                s1="";
                c=1;
            }
            else if(IP[i]=='.' || IP[i]==':'){
                l.push_back(s1);
                s1="";
                c+=1;
            }
            else
                s1+=IP[i];
        }
        l.push_back(s1);
        
        
        if(!(c==3 || c==7))
            return "Neither";
        else{
            if(f==1)
                return ipv4(l);
            else if(f==2)
                return ipv6(l);
            else
                return "Neither";
        }
    }
};
