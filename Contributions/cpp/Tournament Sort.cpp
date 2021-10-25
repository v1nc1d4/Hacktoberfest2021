#include<iostream>
#include<time.h>
#include<stdlib.h>
using namespace std;

class tournamet
{
    
    public:
    //tournament works so much like heapsort 
    //in this we will also make a heap 
    //it will make a min heap
    void random(int arr[],int n)
	{
       srand(time(0));
	   for(int i=0;i<=n;i++)
	   {
	   	 arr[i] = rand()%100 + 1;
	   }	
	}
    void sorted(int array[],int num)
        {
            //it  will divide total number of elements from 2
            //it will start checking from 
            for (int i = num / 2; i >= 0; i--)
            {
                swapping(array, num, i);
            }
            //it will remove element from one by one
            //means one by one palyers getting out from the tournament
            for (int i = num - 1; i >= 0; i--)
            {
                if (array[0] > array[i])
                {
                    // swapping current root to end
                    int swap = array[0];
                    array[0] = array[i];
                    array[i] = swap;
                    swapping(array, i, 0);
                }

            }
            //call min heapify on the reduced heap
        }
        void swapping(int arr[], int n, int k)
        {
            int minimum = k;//we are initializing that the the minimum is the root ;
            int left = 2 * k;//the left child is 2*k index;
            int right = 2 * k + 1;//the right child is 2*k+1 index
                //it works 
                if (left < n && arr[left] > arr[minimum])
                    minimum = left;//if the left child is lesser than the root it will become a root;


                if (right < n && arr[right] > arr[minimum])
                    minimum = right;//if the right child is lesser than the root than it willl become an root;


                //if the  root is not minimum

                if (minimum != k)
                {
                    int temp = arr[k];//if the root is not minimum then we will swap the root with its minimum child.
                    arr[k] = arr[minimum];
                    arr[minimum] = temp;
                    swapping(arr, n, minimum);

                }
        }
        void printArray(int arr[],int n)
        {
            for (int i = 0; i < n; i++)
            cout<<arr[i]<<" ";
        }
    };

//This is the main function
int main()
{
    int n; //size of the array
    //we will sort this array
    cout<<"Enter the size of array: ";
    cin>>n;
    int arr[n];
    tournamet ob;
    cout<<"Before sorting: ";
    ob.random(arr,n);
    ob.printArray(arr,n);
    cout<<"Sorted array is: ";
    ob.sorted(arr,n);
    ob.printArray(arr,n);
}
