#include <stdio.h>
#define Max(a,b) ((a>b)?a:b)
#define Max_DEGREE 50

typedef struct {
	int degree;
	float coef[MAX_DEGREE];
} polynomial;

int main(void) {
	polynomial A = { 3, {4,3,5,0} };
	polynomial B = { 4, {3,1,0,2,1 } };
	polynomial C;

	C = addPoly(A, B);
	printf("\n A(x) ="); printfPoly(A)
	printf("\n (x) ="); printfPoly(A)
	printf("\n A(x) ="); printfPoly(A)