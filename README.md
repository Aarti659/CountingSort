//C++ Program for Counting sort

#include <iostream.h>

using namespace std;


static void countsort(int Arr[], int n) {
  int max = 0;
  
  
  for (int i=0; i<n; i++) {  
    if(max < Arr[i]) {
      max = Arr[i];
    } 
  }

  
  int freq[max+1];
  for (int i=0; i<max+1; i++) {  
    freq[i] = 0;
  } 
  for (int i=0; i<n; i++) {  
    freq[Arr[i]]++;
  } 
  
  
  for (int i=0, j=0; i<=max; i++) {  
    while(freq[i]>0) {
      Arr[j] = i;
      j++;
      freq[i]--;
    }
  } 
}


static void PrintArray(int Arr[], int n) { 
  for (int i=0; i<n; i++) 
    cout<<Arr[i]<<" "; 
  cout<<"\n"; 
} 


int main (){
  int MyArr[] = {9, 1, 2, 5, 8, 8, 2, 1, 7, 7};
  int n = sizeof(MyArr) / sizeof(MyArr[0]); 
  cout<<"Original Array\n";
  PrintArray(MyArr, n);

  countsort(MyArr, n);
  cout<<"\nSorted Array\n";
  PrintArray(MyArr, n);
  return 0;
}




