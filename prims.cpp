#include<iostream>
#include<omp.h>
using namespace std;

int main()
{
	int nodes, min = 9999, cost = 0;
	double start_time = omp_get_wtime();
	
	int x, y, nv = 1;
	nodes = 5;
	int visited[10] = {0};
	int edges[nodes][nodes];

	cout<<"Prims algorithm "<<endl;

	int graph[5][5] = {{0,6,8,5,4},{6,0,3,9,1},{8,3,0,9,2},{5,9,9,0,7},{4,1,2,7,0}};

	for(int i=0;i<nodes;i++)
	{
		for(int j=0;j<nodes;j++)
		{
			cout<<graph[i][j]<<"\t";
			edges[i][j] = 0;
		}
		cout<<endl;
	}

	visited[1] = 1;

	while(nv < nodes)
	{
		min = 9999;
		for(int i=0;i<nodes;i++)
		{
			if(visited[i]==1)
			{
				#pragma omp parallel for
				for(int j=0;j<nodes;j++)
				{
					if(visited[j]==0 && graph[i][j]!=0)
					{
						#pragma omp critical
						if(min > graph[i][j])
						{
							min = graph[i][j];
							x = i;
							y = j;
						}
					}
				}
			}
		}
		cout<<"\n(v"<<x<<",v"<<y<<")->"<<min;
		cost+= min;
		edges[x][y] = edges[y][x] = min;
		visited[y] = 1;
		nv++;
	}
	cout<<"\n\nAdjacency matrix of MST : \n";
	for(int i=0;i<nodes;i++)
	{
		cout<<"\t";
		for(int j=0;j<nodes;j++)
		{
			cout<<edges[i][j]<<"\t";
		}
		cout<<endl;
	}
	cout<<"Total cost of MST = "<<cost<<endl;
	cout<<"Total execution time : "<<omp_get_wtime() - start_time;
	cout<<endl;
	return 0;
}



