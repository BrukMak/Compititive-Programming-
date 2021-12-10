#include<iostream>
using namespace std;

int main()
{
    int n, m, a;
    cin >> n ;
    cin >> m;
    cin>>a;
    
long long int row ,col;
    
    if(n%a == 0)
      col = n/a;
      else col = n/a +1;
   
        if (m%a == 0){
             row =m/a;
        }
        else row = m/a +1;
      
      
      
      cout<< row*col;
    
    return 0;
}