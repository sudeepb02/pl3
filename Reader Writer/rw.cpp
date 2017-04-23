#include<stdio.h>
#include<time.h>
#include<omp.h>
#include<iostream>
#include<unistd.h>

using namespace std;
int main()
{
	int rthreads, wthreads;
	int readCount = 0;

	cout<<"Enter the number of reader threads : ";
	cin>>rthreads;
	cout<<"Enter the number of writer threads : ";
	cin>>wthreads;

	omp_lock_t writelock;
	omp_init_lock(&writelock);

	int tid;
	int var = 100;

	#pragma omp parallel
	#pragma omp for nowait
	for(int i=0;i<rthreads;i++)
	{
		tid = omp_get_thread_num();
		time_t rawtime;
		struct tm *timeinfo;

		time(&rawtime);
		timeinfo = localtime(&rawtime);
		cout<<"Current local time and date "<<asctime(timeinfo);
		sleep(2);

		cout<<"\nReader "<<i<<" is trying to enter the database for reading data";

		omp_set_lock(&writelock);
		readCount++;
		if(readCount == 1)
		{
			cout<<"\nValue of var = "<<var<<endl;
		}

		omp_unset_lock(&writelock);
		readCount--;
		if(readCount==0)
		{
			cout<<"\nReader "<<i<<" is leaving the datbase\n";
		}
	}

	#pragma omp parallel shared(tid)
	#pragma omp for nowait
	for(int i=0;i<wthreads;i++)
	{
		tid = omp_get_thread_num();
		cout<<"\nWriter thread "<<i<<" is trying to enter the database ";

		omp_set_lock(&writelock);
		var+= 100;
		cout<<"\nNew value of var = "<<var;

		cout<<"\nWriter thread "<<i<<" is leaving the database"<<endl;

		omp_unset_lock(&writelock);
	}
	cout<<endl;

	omp_destroy_lock(&writelock);
	return 0;
}


