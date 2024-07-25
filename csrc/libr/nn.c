#include "stdlib.h"

struct matrix {
    double* value;
    int rows;
    int columns;
} matrix;

struct vector {
    double* value;
    int nvals;
} vector;

struct data {
    double* matrix;
} data;

struct batch {
    double* matrix;
} batch;

struct layer {
    struct matrix* w;
    struct vector* b;

    struct matrix* dw;
    struct vector* dv;

    double (* activation)(double)

} layer;

struct nn {
    struct layer** layers;
    double (*loss) (double, double);
    double (* optimizer)(double, double);

} nn;

struct train_nn {
    struct nn* model;
    int num_epochs;
} nn;