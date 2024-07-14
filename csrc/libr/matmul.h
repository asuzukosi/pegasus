double dotproduct(const double *a, const double *b, int size);
double * getrowvector(const double *a, int rowsize, int colsize, int rowindex);
double * getcolumnvector(const double *a, int rowsize, int colsize, int index);
void printvector(const double *a, int size);
void printmatrix(const double *a, int numrows, int numcolumns);
double* transposematrix(const double *a, int rowsize, int colsize);