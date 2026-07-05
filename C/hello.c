// hello.c
// Simple C program with a helper function demonstration.

#include <stdio.h>

void print_block(int height);

int main(void)
{
    printf("Hello, world!\n");
    print_block(3);
    return 0;
}

void print_block(int height)
{
    for (int i = 0; i < height; i++)
    {
        printf("#\n");
    }
}
