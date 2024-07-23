#include "matmul.h"
#include "stdlib.h"
#include "stdio.h"

double add(double x, double y){
    return x + y;
}

int main(int argc, char **argv){
    // testing vector dot product
    double a[2][2] = {{1, 2},
                      {3, 4}};

    
    double b[2][2] = {{1, 1},
                      {1, 1}};
    
    double v[2] = {1, 2};

    // double* c = matrixmultiply((double *)a, 2, 2, (double *)b, 2, 2);

    // double* d = scalar_matrix_op((double *)b, 2, 2, add , 5);
    double* d = vector_matrix_op((double *)a, 2, 2, (double *)v, 2, 1, add);

    printmatrix(d, 2, 2);
    free(d);
    // double* c = transposematrix((double*)a, 2, 2);

    // printmatrix((double*)a, 2, 2);
    // printf("\n");
    // printmatrix((double*)c, 2, 2);
    // double *arr = getcolumnvector((double *)a, 2, 2, 2);
    // printvector(arr, 2);
    // free(arr);

    // TODO: test creation of 2d array with malloc
}