from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
root = 0

data_to_scatter = []
if rank == root:
    # If I am the root, generate data.
    data_to_scatter = [i for i in range(size)]
    print("We will be scattering: ", data_to_scatter)


# Each node receives one element of data_to_scatter
scattered_data = comm.scatter(data_to_scatter, root=root)
print("Rank ", rank, "has data: ", scattered_data)

# Process scattered data
scattered_data = scattered_data + 1

# Gather
gathered_data = comm.gather(scattered_data, root=root)
if rank == root:
    print("The gathered result is: ", gathered_data)
