#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<string> names = {"Alice", "Bob", "Charlie"};
    for (const auto &n : names)
        cout << "Hi " << n << endl;
    return 0;
}