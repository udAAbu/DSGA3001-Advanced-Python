
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

value = np.zeros(1)

if rank >= 1:
    #for r >= 1, receive the value from r - 1
    comm.Recv(value, source = rank - 1)
    #update its value
    value += rank ** 2
    
    #send the value to process r + 1, for process N-1, send the value to process 0
    if rank != size - 1:
        comm.Send(value, dest = rank + 1)
    else:
        comm.Send(value, dest = 0)
else:
    #for r = 0, first send its value to r = 1
    comm.Send(value, dest = 1)
    
    #receive the value from process N-1
    comm.Recv(value, source = size - 1)
    print("Process: {}, received value: {}".format(rank, value[0]))
