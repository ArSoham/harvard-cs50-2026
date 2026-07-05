// arrays.c
// Demonstrates array input and average calculation in C.

#include <stdio.h>

#define NUM_SCORES 3

float average(int length, int scores[]);

int main(void)
{
    int scores[NUM_SCORES];

    // Read scores from the user
    for (int i = 0; i < NUM_SCORES; i++)
    {
        printf("Score %d: ", i + 1);
        scanf("%d", &scores[i]);
    }

    // Print the average of the scores
    printf("Average: %.2f\n", average(NUM_SCORES, scores));
    return 0;
}

float average(int length, int scores[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += scores[i];
    }
    return sum / (float) length;
}
