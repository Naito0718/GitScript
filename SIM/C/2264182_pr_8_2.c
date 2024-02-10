
#include<stdio.h>
#include <string.h>

int main(void)
{
float max;
char maxPlayer[50];
struct student
   {
      char name[50];
      float gpa;
   };

struct student dnj[5];
max=0.0;

for (int i = 0; i < 5; i++)
{
    printf("No.%3d : \n",i+1); 
    printf("Name = \n"); scanf("%s",dnj[i].name); 
    printf("Score = \n"); scanf("%f",&dnj[i].gpa); 

    if (dnj[i].gpa>max)
    {
        max=dnj[i].gpa;
        strcpy(maxPlayer, dnj[i].name);
    }
    
}

printf("max GPA Player= %s, max GPA=%f",maxPlayer,max);

return 0;
}

/*文字列のコピーができなかったので、strcpy関数を用いた。*/

/*No.  1 : 
Name =
Tanaka
Score =
3.4
No.  2 :
Name =
Yoshida
Score =
2.5
No.  3 :
Name =
Ida
Score =
4.2
No.  4 :
Name =
Taguchi
Score =
3.9
No.  5 :
Name =
Kato
Score =
3.7
max GPA Player= Ida, max GPA=4.200000*/
