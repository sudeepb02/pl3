#include<iostream>
#include<unistd.h>
#include<sys/types.h>
#include<sys/shm.h>
#define SIZE 30
using namespace std;

int square(int k)
{
	int a, b;
	a = k/10;
	b = k%10;

	int sq = a*a*100 + a*b*2*10 + b*b;
	return sq;
}

int main()
{
	int shmid;
	key_t key = 5678;

	//Initialize shared memory
	shmid = shmget(key, SIZE, IPC_CREAT);
	if(shmid<0)
	{
		cout<<"Error initializing shared memory"<<endl;
	}
	else
	{
		cout<<"Shared memory initialized successfully"<<endl;
	}

	char *s,*shm;

	//Attaching segment
	if((shm=(char*)shmat(shmid,NULL,0))==0)
	{
		cout<<"Error attaching segment"<<endl;
	}
	else
	{
		cout<<"Segment attached successfully"<<endl;
	}

	//Wait until the number is stored by client in shared memory
	while(*shm!='*')
	{
		sleep(1);
	}

	s = shm;	//Top of shared memory
	s++;		//Point to next location
	int number = (int)*s;		//Get the number from client
	int sq = square(number);	//Calculate square
	
	//Write result to shared memory
	s = shm;
	s++;
	int a = 1000;
	for(int i=0;i<4;i++)
	{
		*s = (char)(sq/a + 48);		//Convert to ascii and store
		sq = sq%a;
		a = a/10;
		s++;
	}
	*s = '^';		//Indicate end of result to client

	//Wake up client
	*shm = '%';

	//Confirm that data is read by client
	while(*shm!='$')
	{
		sleep(1);
	}

	//Detach and return

	return 0;

}
