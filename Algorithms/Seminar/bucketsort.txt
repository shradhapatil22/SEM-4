#include <stdio.h>
#include <stdlib.h>

 //C program to sort an
// array using bucket sort
// Function to sort arr[] of
// size n using bucket sort
//insertion sort
 void sort(float arr[],int n)
 {
    int j;
    float k;
    for(int i=0;i<n;i++)
    {
        j=i-1;
        k=arr[i];
    while(j>=0&&arr[j]>k)
    {
        arr[j+1]=arr[j];
        j--;
    }
    arr[j+1]=k;

    }
 }

 //bucket sort
void bucketSort(float arr[], int n)
{

     float b[n][n];
     int len[n];
     for(int i=0;i<n;i++){
        len[i]=0;
     }

    // 2) Put array elements
    // in different buckets
    for (int i = 0,j=0; i < n; i++) {
        int bi = n * arr[i]; // Index in bucket
        ++len[bi];
        b[bi][len[bi]-1]=arr[i];

    }

    // 3) Sort individual buckets
    for (int i = 0; i < n; i++)
        sort(&b[i],len[i]);

    // 4) Concatenate all buckets into arr[]
    int index = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j <len[i]; j++)
            arr[index++] = b[i][j];
}

/* Driver program to test above function */
int main()
{
    float arr[10];
    int n;
    printf("enter the no of elements\n");
    scanf("%d",&n);
    printf("enter the array elements\n");
    for(int i=0;i<n;i++)
    {
        scanf("%f",arr+i);
    }
    bucketSort(arr, n);

    printf("sorted array is \n");
    for (int i = 0; i < n; i++)
       printf("%f\t",arr[i]) ;
    return 0;
}
