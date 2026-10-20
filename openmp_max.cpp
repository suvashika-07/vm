#include <iostream>
#include <omp.h>
using namespace std;

int main() {
    int arr[] = {12, 45, 23, 89, 34, 67};
    int n = 6;
    int maximum = arr[0];

    #pragma omp parallel for reduction(max:maximum)
    for (int i = 0; i < n; i++) {
        if (arr[i] > maximum) {
            maximum = arr[i];
        }
    }

    cout << "Maximum number: " << maximum << endl;

    return 0;
}