//-----Abhishek Chaudhary------
//----Student at IIT Jammu-----
#include<bits/stdc++.h>
#define differ(a,b) a<b ? b-a:a-b
using namespace std;
int main(){
	int  n,m,k,l,r,t,c,p,min_price,temp;
	cin>>t;
	while(t--){
		cin>>n>>m>>k>>l>>r;
		min_price=-1;
		for(int i=0;i<n;i++){
			cin>>c>>p;
			if(min_price!=-1 and p>=min_price)
				continue;
			int tem=differ(c,k);
			if(tem<=m)
				temp=k;
			else if(c<k)
				temp=c+m;
			else
				temp=c-m;
			if(temp>=l && temp<=r)
				min_price=p;
		}
		cout<<min_price<<endl;
	}
	return 0;
}