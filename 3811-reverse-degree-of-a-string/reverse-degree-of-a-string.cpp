
class Solution {
public:
    int reverseDegree(string s) {
        string s1="zyxwvutsrqponmlkjihgfedcba";
        int sum=0;
        for(int i=0;i<s.size();i++){
            sum+=(s1.find(s[i])+1)*(i+1);
        }
        return sum;
    }
};