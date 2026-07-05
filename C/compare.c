// compare.c
// Reads two integers and compares their values.

#include <stdio.h>

int main(void)
{
    int x, y;

    printf("Enter two integers: ");
    scanf("%d %d", &x, &y);

    if (x < y)
    {
        printf("%d is less than %d
", x, y);
    }
    else if (x > y)
    {
        printf("%d is greater than %d
", x, y);
    }
    else
    {
        printf("%d and %d are equal
", x, y);
    }

    return 0;
}
