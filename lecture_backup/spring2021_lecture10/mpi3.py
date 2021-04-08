#####
# Sending a message from one process to another
#####
import numpy

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

if rank == 1:
        print("part of Process", rank, "- before receiving has the number", randNum[0])
        # generates a numpy array with one element unif. distr. from [0,1)
        randNum = numpy.random.rand(1)
        print("part of Process", rank, "- drew the number", randNum[0])
        comm.Send(randNum, dest=0)
        
        print("Here")
        
if rank == 0:
        incoming = numpy.zeros(1)
        print("part of Process", rank, "- before receiving has the number", incoming[0])
        comm.Recv(incoming, source=1)
        print("part of Process", rank, "- received the number", incoming[0])
