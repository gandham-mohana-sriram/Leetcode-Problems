class Solution {
public:
    void solve(int op,int cl,int n,string s,vector<string> &l){
        if(op==n && cl==n){
            l.push_back(s);
            return;
        }
        if(op>cl){
            s.push_back(')');
            solve(op,cl+1,n,s,l);
            s.pop_back();
        }
        if(op<n){
            
            s.push_back('(');
            solve(op+1,cl,n,s,l);
            s.pop_back();
        }


    }
    vector<string> generateParenthesis(int n) {
        vector<string>l;
        string s="";
        solve(0,0,n,s,l);
        return l;
    }
};