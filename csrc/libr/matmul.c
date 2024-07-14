#include "stdlib.h"
#include "stdio.h"

double dotproduct(const double *a, const double *b, int size){
    int sum = 0;
    for(int i = 0; i <  size; i ++){
        sum += a[i] * b[i];
    }
    return sum;
}

double * getrowvector(const double *a, int rowsize, int colsize, int rowindex){
    // create the row vector from a matrix
    if(rowindex >= rowsize){
        printf("row index out of range \n");
        exit(0);
    }
    double *row = malloc(sizeof(double) * colsize);
    int pos;
    for(int i = 0; i < colsize; i++){
        pos = ((rowindex * colsize) + i);
        row[i] = *(a + pos);
    }
    return row;
}

double * getcolumnvector(const double *a, int rowsize, int colsize, int colindex){
    // create the column vector from a matrix
    if(colindex >= colsize){
        printf("column index out of range \n");
        exit(0);
    }
    double *column = malloc(sizeof(double) * rowsize);
    int pos;
    for (int i = 0; i < rowsize; i++){
        pos = ((colsize * i) + colindex);
        column[i] = *(a + pos);
    }
    return column;
}

void printvector(const double *a, int size){
    printf("{ ");
    for(int i=0; i<size; i++){
        printf("%.2f, ", a[i]);
    }

    printf("} \n");
}



void printmatrix(const double *a, int numrows, int numcolumns){
    int pos;
    // printf("{");
    for(int i = 0; i < numrows; i++){
        printf("{");
        for(int j = 0; j < numcolumns; j++){
            pos = (i * numcolumns) + j;
            printf("%.2f,", a[pos]);
        }
        printf("},");
        if(i != numrows - 1)
            printf("\n");
    }
    printf("\n");
}