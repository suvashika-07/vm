from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    arr = [12, 45, 23, 89, 34, 67]
    chunks = [arr[i::size] for i in range(size)]
else:
    chunks = None

local_arr = comm.scatter(chunks, root=0)

local_max = max(local_arr) if local_arr else float('-inf')

max_values = comm.gather(local_max, root=0)

if rank == 0:
    print("Array:", arr)
    print("Maximum number:", max(max_values))