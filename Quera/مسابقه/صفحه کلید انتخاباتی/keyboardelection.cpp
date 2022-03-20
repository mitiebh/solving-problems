#include <iostream>
#include <string>
using namespace std;

int main()
{
    int n,flag=0;
    cin >> n;
    string input,temp;
    string store_input[150];
    string name[150];
    for (int i = 0; i < n; i++)
    {
        cin >> input;
        store_input[i] = input;
    }
    for (int i = 0; i < n; i++)
    {
        if (store_input[i] == "CAPS" && flag == 0)
        {
            for (int j = i+1; store_input[j] != "CAPS" && j<n; j++,i++)
            {
                temp = store_input[j];
                name[i] = toupper(temp[0]);
            }
            flag = 1;
        }
        else if (store_input[i] == "CAPS" && flag == 1)
        {
            for (int j = i+1; store_input[j] != "CAPS" && j<n; j++,i++)
            {
                temp = store_input[j];
                name[i] = tolower(temp[0]);
            }
            flag = 0; 
        }
        else
        {
            name[i] = store_input[i];
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << name[i] << "";
    }
    cout << endl;
}