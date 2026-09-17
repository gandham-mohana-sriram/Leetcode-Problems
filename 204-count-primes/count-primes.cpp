const int n=1e6*5+1;
vector<bool>a(n,true);
void seive(){
    a[0]=a[1]=false;
    if (a[4]==false){
        return;
    }
    for(int i=2;i*i<n;i++){
        if (a[i]){
            for(int j=i*i;j<n;j+=i){
                if (a[j])
                a[j]=false;
            }
        }
    }
}
class Solution {
public:
    int countPrimes(int n) {
        seive();
        int c=0;
        for(int i=1;i<n;i++){
            if(a[i]){
                c+=1;
            }
        }
        return c;
    }
};