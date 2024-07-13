#include "stdlib.h"
#include "stdio.h"

double dotproduct(const double *a, const double *b, int size){
    int sum = 0;
    for(int i = 0; i <  size; i ++){
        sum += a[i] * b[i];
    }
    return sum;
}

double * getrowvector(const double *a, int size, int index){
    // create the row vector from a matrix
    double *row = malloc(sizeof(double) * size);
    int pos;
    for(int i = 0; i < size; i++){
        pos = ((index * size) + i);
        row[i] = *(a + pos);
    }
    return row;
}

double * getcolumvector(const double **a, int rowsize, int colsize, int colindex){
    // create the column vector from a matrix
    double *column = malloc(sizeof(double) * rowsize);
    // for (int i = 0; i < size; i++){
    //     column[i] = a[i][index];
    // }
    return column;
}

void printvector(const double *a, int size){
    printf("{ ");
    for(int i=0; i<size; i++){
        printf("%f ,", a[i]);
    }

    printf("} \n");
}