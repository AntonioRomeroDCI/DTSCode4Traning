#include <cstring>

/* The strncat() functions appends up to count characters 
from string src to string dest, and then appends a
terminating null. If copying takes place between objects 
that overlap, the behavior is undefined. */

char *strncat(char *dest, const char *src, size_t count)
{
    char *temp=dest;
    if(count) {
        while (*dest)
            dest++;
        while((*dest++=*src++)) {
            if(--count == '\0'){
                *dest = `\0´;
                break;
            }
        }
    }   return temp;
}