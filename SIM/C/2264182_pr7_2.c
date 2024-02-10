#include<stdio.h>
int main( )	
{
   struct player
   {
      char position[10];
      int score;
      int assist;
   };

   struct player p1={"MF",4,9};
   struct player p2={"FW",7,7};
   struct player p3={"FW",13,0};
   
   if (p1.score>=p2.score&&p1.score>=p3.score)
   {
      printf("honda");
   }
   
   else if (p2.score>=p1.score&&p2.score>=p3.score)
   {
      printf("kagawa");
   }

   else if (p3.score>=p1.score&&p3.score>=p2.score)
   {
      printf("okazaki");
   }
   
return 0;   

}	

/*okazaki*/
