#include<bits/stdc++.h>
using namespace std;

class LinkedList{
	public:
		int val;
		LinkedList* next;
};

LinkedList* head=NULL;

void insert(int x){
	LinkedList* node=new LinkedList();
	node->val=x;
	node->next=head;
	head=node;
}

void print(){
	LinkedList* temp=head;
	while(temp!=NULL){
		cout<<temp->val<<" ";
		temp=temp->next;
	}
}

int main(){
	insert(10);
	insert(9);
	insert(4);
	insert(1);
	cout<<"LinkedList elements are: ";
	print();
	return 0;
}
