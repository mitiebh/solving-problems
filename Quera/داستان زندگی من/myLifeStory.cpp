#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int m1,d1,m2,d2;
    cin >> m1 >> d1;
    cin >> m2 >> d2;

    int p1,p2,result;
    if (m1==m2)
    {
        result = d2-d1;
    }
    else
    {
        // person1
        if (m1 <= 7)
        {
            p1 = ((m1-1)*31) + d1;
        }
        if (m1 > 7 && m1 < 12)
        {
            p1 = (6*31) + ((m1-7)*30) + d1;
        }
        if (m1 == 12)
        {
            p1 = (6*31) + (5*30) + d1;
        }
        // person2
        if (m2 <= 7)
        {
            p2 = ((m2-1)*31) + d2;
        }
        if (m2 > 7 && m2 < 12)
        {
            p2 = (6*31) + ((m2-7)*30) + d2;
        }
        if (m2 == 12)
        {
            p2 = (6*31) + (5*30) + d2;
        }
        result = abs(p1-p2);
    }
    cout << result << endl;
}