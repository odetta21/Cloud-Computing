#include <stdio.h>
#include <limits.h>
#include <bits/stdc++.h>
 


int main(){

	int a[4];
    int v1;
    int v2;
    int v3;
    int v4;
	

    __asm__("mov $0x1 , %eax\n\t");
    __asm__("cpuid\n\t");
    __asm__("mov %%eax, %0\n\t":"=r" (a[0])); //gives model and family
    __asm__("mov %%ebx, %0\n\t":"=r" (a[1])); //gives additional feature info
    __asm__("mov %%ecx, %0\n\t":"=r" (a[2])); //feature flags
    __asm__("mov %%edx, %0\n\t":"=r" (a[3])); //feature flags



    v1 = (a[0]);
    v2 = (a[1]);
    v3 = (a[2]);
    v2 = (a[3]);
      

    printf("la valeur est: %x\n", v1);

    

    cout << "eax : " << bitset<32>(a[0]) << endl;
    cout << "ebx : " << bitset<32>(a[1]) << endl;
    cout << "ecx : " << bitset<32>(a[2]) << endl;
    cout << "edx : " << bitset<32>(a[3]) << endl;
    

    
    return  0;
}