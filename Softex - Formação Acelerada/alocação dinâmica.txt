#include <stdio.h>
#include <locale.h>
#include <stdlib.h>

int main(){
	
	setlocale(LC_ALL, "portuguese");
	
	int i=666 ;
	int *p=(NULL);
	p = realloc(p, 22*sizeof(int));
 	
}
