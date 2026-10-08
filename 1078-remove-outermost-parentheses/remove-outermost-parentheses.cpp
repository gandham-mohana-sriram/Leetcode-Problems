class Solution {
public:
    string removeOuterParentheses(string s) {
        vector<string>l;
        int st=0,en=0;
        int op=0;
        string s1;
        for(int i=0;i<s.size();i++){
        if(s[i]=='('){
            if(op>0) s1+=s[i];
            op+=1;
        }
        else if(s[i]==')'){
            op-=1;
            if(op>0) s1+=s[i];
        }
        }
        return s1;
    }
};