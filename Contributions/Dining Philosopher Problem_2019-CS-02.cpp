#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
#include<unistd.h>
#include<stdlib.h>


sem_t Room;
sem_t sticks[5];

void * Philosopher(void *);
void eat(int);
int main()
{
	int i,a[5];
	pthread_t tid[5];
	
	sem_init(&Room,0,4);
	
	for(i=0;i<5;i++)
		sem_init(&sticks[i],0,1);
		
	for(i=0;i<5;i++){
		a[i]=i;
		pthread_create(&tid[i],NULL,Philosopher,(void *)&a[i]);
	}
	for(i=0;i<5;i++)
		pthread_join(tid[i],NULL);
}

void * Philosopher(void * num)
{
	int phil=*(int *)num;

	sem_wait(&Room);
	printf("\nPhilosopher %d has entered Room",phil);
	sem_wait(&sticks[phil]);
	sem_wait(&sticks[(phil+1)%5]);

	eat(phil);
	sleep(2);
	printf("\nPhilosopher %d has finished eating",phil);

	sem_post(&sticks[(phil+1)%5]);
	sem_post(&sticks[phil]);
	sem_post(&Room);
}

void eat(int phil)
{
	printf("\nPhilosopher %d is eating",phil);
}
