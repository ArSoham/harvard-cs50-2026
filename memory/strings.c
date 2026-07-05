// strings.c
// Demonstrates reading a string, copying it, and capitalizing the first letter.

#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char s[100];

    printf("s: ");
    scanf("%99s", s);

    char t[100];
    strcpy(t, s);
    t[0] = toupper((unsigned char)t[0]);

    printf("s: %s
", s);
    printf("t: %s
", t);
    return 0;
}
