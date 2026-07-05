// exit_status.c
// Demonstrates returning explicit exit codes from the main function.

#include <stdio.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Missing command-line argument
");
        return 1;
    }

    printf("hello, %s
", argv[1]);
    return 0;
}
