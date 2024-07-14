#include "matmul.h"
#include "stdlib.h"
#include "stdio.h"

int main(int argc, char **argv){
    // testing vector dot product
    double a[2][2] = {{1, 2},
                      {3, 4}};
    double* b = (double*)a;

    // printf("testing %f \n", b[0][0]);
    printmatrix((double*)a, 2, 2);
    // double *arr = getcolumnvector((double *)a, 2, 2, 2);
    // printvector(arr, 2);
    // free(arr);

    // TODO: test creation of 2d array with malloc
}