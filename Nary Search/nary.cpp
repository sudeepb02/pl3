#include<iostream>
#include<vector>
#include<omp.h>
using namespace std;
#define THREADS 104

int search(vector<int>, int, int, int);

int main()
{
	vector<int> arr = {2,4,6,7,8,9,11,16,19,23,27,29,36, 39};
	int key;
	double stime;
	int size = arr.size();

	cout<<"Please enter the element to search : ";
	cin>>key;

	stime = omp_get_wtime();
	int pos = search(arr, 0, size - 1, key);

	if(pos!=-1)
	{
		cout<<"Element found at position " <<pos<<endl;
	}
	else
	{
		cout<<"Element not found"<<endl;
	}
	
	cout<<"Execution time : "<<omp_get_wtime() - stime;
	cout<<endl;
	return 0;
}

int search(vector<int> arr, int low, int high, int key)
{
	//Return -1 in case element not found
	int res = -1;


	if(high - low>=THREADS)
	{
		int partsize = (high - low/THREADS) + 1;
		#pragma omp parallel for
		for(int i=0; i<THREADS; i++)
		{
			int nhigh;
			if(((i+1)*partsize - 1) > high)
			{
				nhigh = high;
			}
			else
			{
				nhigh = (i+1)*partsize - 1;
			}
			if(key>=arr[i*partsize] && key<=arr[nhigh])
			{
				res = search(arr, i*partsize, nhigh, key);
			}
		}
	}
	else
	{
		#pragma omp parallel for
		for(int i= low; i<=high; i++)
		{
			if(arr[i] == key)
			{
				res = i;
			}
		}
	}
	return res;
}


