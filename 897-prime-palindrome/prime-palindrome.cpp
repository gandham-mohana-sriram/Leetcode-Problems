#include<string>
const int n=1e8*2+1;
vector<bool>a(n,true);
void seive(){
    a[0]=a[1]=false;
    if (a[4]==false){
        return;
    }
    for(int i=2;i*i<n;i++){
        if (a[i]){
            for(int j=i*i;j<n;j+=i){
                if (a[j]==true)
                a[j]=false;
            }
        }
    }
}
class Solution {
public:
    int primePalindrome(int n) {
        seive();
        while(1){
        if(a[n]==true){
            int b=n,r,s=0;
            while(b!=0){
                r=b%10;
                s=s*10+r;
                b=b/10;
            }
            if(s==n)
            return n;
        }
        n+=1;
    }
    }
};