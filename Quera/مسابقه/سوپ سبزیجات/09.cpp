#include <iostream>
using namespace std;

int main()
{
    int n;
    double k,s;
    double res;
    cin >> n >> k >> s;
    res = n * k;
    if (res <= s)
    {
        cout << "Kafie!";
    }
    else
    {
        cout << "Na! yeki bayad bere sabzi bekhare";
    } 
}