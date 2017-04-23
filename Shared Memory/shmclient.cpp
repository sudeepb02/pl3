#include<iostream>
#include<sys/types.h>
#include<sys/shm.h>
#include<sys/ipc.h>
#include<unistd.h>
#define SIZE 30
using namespace std;

int main()
{
	int shmid, number;
	char *shm, *s, noch;
	key_t key = 5678;

	//Initialize shared memotry
	shmid = shmget(key, SIZE, IPC_CREAT|0666);
	if(shmid<0)
	{
		cout<<"Error initializing shared memory"<<endl;
	}
	else
	{
		cout<<"Shared memory Initialized successfullu"<<endl;
	}

	//Attach segment
	if((shm=(char*)shmat(shmid,NULL,0))==0)
	{
		cout<<"Erro attaching segment"<<endl;
	}
	else
	{
		cout<<"Segment attached successfully"<<endl;
	}

	//Get the number
	cout<<"Enter a number to be squared : ";
	cin>>number;

	//Convert the number into character to store in shared memory
	noch = (char)number;

	s = shm;	//Top of shared memory
	s++;		//next memory location
	*s = noch;	//Store the number at next memory location

	//Indicate that the number is stored by client by setting top of shm as *
	*shm = '*';

	//Wait for server until result is written
	while(*shm!='%')
	{
		sleep(1);
	}

	//Read the result and write to screen
	s = shm;
	s++;
	for(int i=0;i<4 && *s!='^';i++)
	{
		cout<<*s;
		s++;
	}

	//Signal that result is displayed
	*shm = '$';

	return 0;
}
