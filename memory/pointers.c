// pointers.c
// Demonstrates the relationship between a variable and its pointer.

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;

    printf("Value of n: %d
", n);
    printf("Address of n: %p
", (void *)p);
    printf("Value through pointer: %d
", *p);
    return 0;
}
