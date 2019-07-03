#include <stdio.h>


int * readFromFile(char file_name[] , int * cores  ){
    int columns = 0 ;
    int index = 0 ;
	int first , second , third ;
    FILE * file = fopen (file_name ,"r");

    fscanf (file, "%d\n", cores);//Read Number of Cores
    fscanf (file, "%d\n", &columns);//Read Number of Columns
    int i = 0 ;
    int * numbers = (int *)malloc(sizeof(int) * (columns * 3) );
    for ( i = 0 ; i < columns ; i++){
        
        fscanf (file, "%d %d %d\n", &first,&second,&third);
        numbers[index++] = first ;
        numbers[index++] = second ;
        numbers[index++] = third ;
    }

    return numbers ;

}


int main(){
    int  cores = 0 ;
    int * numbers = readFromFile("C:\\Users\\Hossein\\Desktop\\hi.txt" , &cores);
    printf("Cores : %d" , cores );

    int i = 0 ;
    for ( i = 0 ; i < 9 ; i++){
        printf("%d\n",numbers[i]);
    }

    return 0 ;

}

