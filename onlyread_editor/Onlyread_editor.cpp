#include<iostream>
#define ull unsigned long long
#define ll long long
#define __luogu__ 0
#if __luogu__==0
#define getchar_unlocked _getchar_nolock
#endif
using namespace std;

string s;
int d;

int main(){
	printf("Only-read config editor\n");
	while(1){
		printf("\nfile name:");
		cin >> s;
		printf("enter 0 to remove only-read, 1 to add it:");
		cin >> d;
		if(d==0){
			string com="attrib "+s+" -r";
			system(com.c_str());
		}
		else if(d==1){
			string com="attrib "+s+" +r";
			system(com.c_str());
		}
		else{
			printf("please enter 0 or 1!\n");
		}
	}
	return 0;
}
