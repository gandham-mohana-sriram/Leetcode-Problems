const int n=31622+1;
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
    int nonSpecialCount(int l, int r) {
        seive();
        int c=0;
        int x=(r-l+1)-c;
        int ma= sqrt(r);
        int mi= ceil(sqrt(l));
        for(int i=mi;i<=ma;i++){
            if(a[i])
            c++;
        }
        return x-c;
    }
};