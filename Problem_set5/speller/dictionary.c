// dictionary.c
// Implements a hash table data structure for CS50's dictionary project.

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table based on dictionary size
const unsigned int N = 26;

// Hash table
node *table[N];

bool check(const char *word)
{
    // TODO: Search for word in hash table and return true if found
    return false;
}

unsigned int hash(const char *word)
{
    // TODO: Improve this hash function for better distribution
    return toupper((unsigned char)word[0]) - 'A';
}

bool load(const char *dictionary)
{
    // TODO: Load dictionary into hash table
    return false;
}

unsigned int size(void)
{
    // TODO: Return number of words in dictionary
    return 0;
}

bool unload(void)
{
    // TODO: Free all memory used by dictionary
    return false;
}
