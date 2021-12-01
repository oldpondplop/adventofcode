#include <stdio.h>
#include <stdlib.h>

int part1(int *arr,int len);
int part2(int *arr,int len);

int main()
{
    FILE *fp = fopen("inp_d1.txt", "r");

    int num,len=2000;
    int *arr = (int* ) malloc (len * sizeof(int));

    if (!fp) {
        printf("no file error!");
        exit(-1);
    } else {
        int i=0;
        while ((fscanf(fp,"%d",&num)) != EOF) {
            arr[i]=num;
            i++;
        }
    }

    fclose(fp);
    part2(arr,len);
    free(arr);
    
    return 0;
}

int part1(int *arr,int len){
    int cnt = 0;
    for (int i=0;i<len-1; i++){
        if (arr[i]<arr[i+1]){
            cnt++;
        }
    }
    printf("%d", cnt);
}

int part2(int *arr,int len){
    int cnt = 0;
    int prev=0;
    for (int i=0;i<len-2; i++){
        int three_sum=0;
        for (int j=0; j<3; j++){
            three_sum+=arr[i+j];
        }
        if (prev < three_sum && prev != 0){
            cnt++;
        }
        prev = three_sum;
    }
    printf("%d", cnt);
}
