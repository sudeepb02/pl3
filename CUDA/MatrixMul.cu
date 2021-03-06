//Matrix Multiplication
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 2
#define GRID_SIZE 2
#define N GRID_SIZE * BLOCK_SIZE

__global__ void MatrixMul(float *A, float *B, float *C, int n)
{
	// Each thread computes a single element of C
	int row = blockIdx.y*blockDim.y + threadIdx.y;
	int col = blockIdx.x*blockDim.x + threadIdx.x;

	float sum = 0;
	for (int i = 0; i < n; ++i) {
		sum += (A[row*n + i] * B[i*n + col]);
	}
		
	C[row*n + col] = sum;
	printf("\n Block[%d][%d] : Thread[%d][%d] : Product = %.2f\n", blockIdx.x, blockIdx.y, threadIdx.x, threadIdx.y, sum);
}

int main()
{
	// Perform matrix multiplication C = A*B
	// where A, B and C are NxN matrices
	// Restricted to matrices where N = GRID_SIZE*BLOCK_SIZE;
	float *hA, *hB, *hC;
	float *dA, *dB, *dC;
	int size = N * N * sizeof(float);

	printf("Matrix Multiplcation:-->\n");
	printf("Matrix size: %d x %d\n", N,N);

	// Allocate memory on the host
	hA = (float *) malloc(size);
	hB = (float *) malloc(size);
	hC = (float *) malloc(size);

	// Initialize matrices on the host
	for (int j = 0; j<N; j++){
		for (int i = 0; i<N; i++){
			hA[j*N + i] = 3;
			hB[j*N + i] = 2;
		}
	}

	printf("Matrix 1:\n");
	for (int j = 0; j<N; j++){
		for (int i = 0; i<N; i++){
			printf("%.2f ", hA[j*N + i]);
		}
		printf("\n");
	}
	
	printf("\nMatrix 2:\n");
	for (int j = 0; j<N; j++){
		for (int i = 0; i<N; i++){
			printf("%.2f ", hB[j*N + i]);
		}
		printf("\n");
	}
	// Allocate memory on the device
	cudaMalloc(&dA, size);
	cudaMalloc(&dB, size);
	cudaMalloc(&dC, size);

	dim3 threadBlock(BLOCK_SIZE, BLOCK_SIZE);
	dim3 grid(GRID_SIZE, GRID_SIZE);

	// Copy matrices from the host to device
	cudaMemcpy(dA, hA, size, cudaMemcpyHostToDevice);
	cudaMemcpy(dB, hB, size, cudaMemcpyHostToDevice);

	//Execute the matrix multiplication kernel
	printf("\n Kernel Launch with Gird of size (%dx%d) and Block of size (%dx%d)\n", GRID_SIZE, GRID_SIZE, BLOCK_SIZE, BLOCK_SIZE);
	MatrixMul <<<grid, threadBlock >>>(dA, dB, dC, N);

	// Now copy the GPU result back to CPU
	cudaMemcpy(hC, dC, size, cudaMemcpyDeviceToHost);

	printf("\nThe Product of Matrix A and B is:\n");
	for (int j = 0; j<N; j++){
		for (int i = 0; i<N; i++){
			printf("%.2f ", hC[j*N + i]);
		}
		printf("\n");
	}
	return 0;
}
