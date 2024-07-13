#include "matmul.h"
#include "stdlib.h"
#include "stdio.h"

int main(int argc, char **argv){
    // testing vector dot product
    double a[2][2] = {{1, 2},
                      {3, 4}};
    double** b = (double**)a;

    // printf("testing %f \n", b[0][0]);

    double *arr = getrowvector(a, 2, 1);
    printvector(arr, 2);
    free(arr);
}