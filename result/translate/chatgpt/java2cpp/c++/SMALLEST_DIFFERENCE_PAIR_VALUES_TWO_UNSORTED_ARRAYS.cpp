#include <algorithm>
using namespace std;

int f_gold(int A[], int B[], int m, int n) {
    int* copyA = new int[m];
    int* copyB = new int[n];
    copy(A, A + m, copyA);
    copy(B, B + n, copyB);
    
    sort(copyA, copyA + m);
    sort(copyB, copyB + n);
    
    int a = 0, b = 0;
    int result = INT_MAX;
    
    while(a < m && b < n) {
        if(abs(copyA[a] - copyB[b]) < result) 
            result = abs(copyA[a] - copyB[b]);
        
        if(copyA[a] < copyB[b]) 
            a++;
        else 
            b++;
    }
    
    delete[] copyA;
    delete[] copyB;
    
    return result;
}