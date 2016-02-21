#include "heapManage.h"

using namespace std;

int main()
{
    int arrIN[] = {98, 17, 38, 19, 22, 69, 45, 12, 65, 359, 984, 65, 32, 36, 94, 76, 29, 68, 61, 62, 54, 58, 98, 456};
    heapSort(arrIN, sizeof(arrIN)/sizeof(int));
    cout << "Hello world!" << endl;
    return 0;
}
