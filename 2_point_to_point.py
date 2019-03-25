# This program makes each rank sends its data to the next rank
# The last rank sends data to 0
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# A dummy array to send
my_data = [rank for i in range(0, 9)]

print("Hello, World! My rank is: " + str(comm.rank))

if rank == 0:
    comm.send(my_data, dest=rank+1)
    recv_data = comm.recv(source = size -1)

elif 0 < rank < size - 1:
    comm.send(my_data, dest=rank + 1)
    recv_data = comm.recv(source = rank - 1)
else:
    comm.send(my_data, dest=0)
    recv_data = comm.recv(source=rank - 1)

print("My rank is " + str(rank))
print("I received the data: ")
print(recv_data)
