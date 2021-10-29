#include <iostream>
#include <cmath>
#include <vector>
class Stack
{
    public:
        int sizeOfHeap;
        std::vector <int> heapTab;



        void Kill()
        {

            Stack::~Stack;
        }

        void Heapify(int sizeOfHeap, int i)
        {
            int largest = i;
            int l = 2*i+1;
            int r = 2*i+2;

            if(l < sizeOfHeap && heapTab[l] > heapTab[largest]) largest = l;
            if(r < sizeOfHeap && heapTab[r] > heapTab[largest]) largest = r;
            if(largest != i)
            {
                std::swap(heapTab[i], heapTab[largest]);

                Heapify(sizeOfHeap,largest);
            }
        }

        void HeapSort()
        {
            for(int i = (sizeOfHeap /2) - 1; i>=0 ; i--)Heapify(sizeOfHeap,i);
            for(int i = sizeOfHeap - 1; i>=0 ; i--)
            {
                std::swap(heapTab[0],heapTab[i]);
                Heapify(i,0);
            }

        }




        void PrintHeap()
        {
            for(int i = 0 ;  i < sizeOfHeap ; ++i)std::cout<<heapTab[i]<<" ";
            std::cout<<std::endl;
        }

};


int main()
{
    Stack object;
    int choice;


    std::cout<< " type size of binary tree" <<std::endl;
    std::cin>>object.sizeOfHeap;

    for(int i = 0 ; i < object.sizeOfHeap ; i++)
    {
        int value;
        std::cout<<"You add " <<i+1<<" object"<<std::endl;
        std::cin>>value;
        object.heapTab.push_back(value);
    }

    object.PrintHeap();
    std::cout<<"\n\n"<<std::endl;

    object.HeapSort();

    std::cout<<"sorted array"<<std::endl;
    object.PrintHeap();

    object.Kill();

    return 0;
}
