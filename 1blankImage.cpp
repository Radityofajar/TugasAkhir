#include <iostream>
#include "box.h"

using namespace std;

/**
 * Calculate and print the volume of a box.
 */
int main()
{
    box package{ 12, 12, 1 };
    cout << "Package length: " << package.length << endl;
    cout << "Package width:  " << package.width << endl;
    cout << "Package height: " << package.height << endl;
    cout << "Package volume: " << package.volume() << endl;
}