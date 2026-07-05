// buggy.c
// Learning notes from early CS50 debugging practice.
// This file contains corrected examples and comments about common mistakes.

#include <stdio.h>

int main(void)
{
    printf("Hello, world
");
    return 0;
}

// Notes:
// - Missing or misspelled headers like <studio.h> cause compilation failures.
// - Using get_string requires #include <cs50.h> and a properly declared variable.
// - A semicolon is required at the end of each statement.
// - Correct use of printf requires matching format specifiers and arguments.
