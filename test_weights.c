
#include <stdio.h>
#include <stdlib.h>

int read_txt(char* fname, float** array, int nrows, int ncols)
{
    FILE* f;

    printf("Reading: %s\n", fname);
    f = fopen(fname, "r");

    if (f == NULL)
    {
        printf("Could not open file.");
        return 1;
    }

    for(int i=0; i<nrows; i++)
    {
        for(int j=0;j<ncols; j++)
        {
            fscanf(f, "%e", &array[i][j]);
        }
    }

    fclose(f);
    return 0;
}

int main(char *argv[])
{
    int error;
    char fname[256] = "weights.txt";
    float** weights;
    
    weights = (float**)malloc(ROWS*sizeof(float*));
    for(int i=0; i<ROWS; i++)
    {
        weights[i] = (float*)malloc(COLS*sizeof(float));
    }

    error = read_weights(fname, weights);
    if (error != 0) return error;

    for(int i=0; i<ROWS; i++)
    {
        free(weights[i]);
    }
    free(weights);
    
    return 0;
}
