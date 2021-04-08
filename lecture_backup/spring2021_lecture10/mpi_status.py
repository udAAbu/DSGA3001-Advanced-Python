#####
# Sending a message from one process to another
#####


import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

info = MPI.Status()
# print("info: ", info)

randNum = numpy.zeros(1)

if rank == 1:
        randNum = numpy.random.random_sample(1)
        print("Process", rank, "drew the number", randNum[0])
        comm.Send(randNum, dest=0)

if rank == 0:
        print("Process", rank, "before receiving has the number", randNum[0])
        comm.Recv(randNum, source=MPI.ANY_SOURCE, status=info)
        print("Process", rank, "received the number", randNum[0], "from Process", info.Get_source())
