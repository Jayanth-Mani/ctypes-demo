#include <stdio.h>
#include <stdlib.h>

void free_memory(void *ptr)
{
    free(ptr);
    printf("Memory freed!\n");
}
int *arrayAdd(int *nums1, int *nums2, int numsLen)
{
    int *returnArr = (int *)malloc(numsLen * sizeof(int));
    if (returnArr == NULL)
    {
        printf("Oh No! Memory failed to allocate!");
    }
    for (int i = 0; i < numsLen; i++)
    {
        *(returnArr + i) = *(nums1 + i) + *(nums2 + i);
    }
    return returnArr;
}