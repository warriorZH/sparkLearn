#include "CPPStack.h"
#include "quickSort.h"


using namespace std;

int main()
{
    int arrIn[] = {36,34,67,44,78,89,33,48,76,3,8,6,9,45,87};
    quickSort(arrIn, sizeof(arrIn)/sizeof(int));

    return 0;
}
