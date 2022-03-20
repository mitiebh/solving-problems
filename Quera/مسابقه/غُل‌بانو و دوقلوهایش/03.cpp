#include <iostream>
#include <string>
using namespace std;

int main()
{
    string gol1,gol2;
    cin >> gol1;
    for (int i = 0; i < gol1.length()/2; i++)
    {
        swap(gol1[i],gol1[gol1.length()-i-1]);
    }
    gol2 = gol1;
    cout << gol2;
}