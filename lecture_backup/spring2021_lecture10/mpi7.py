#####
# overlap communication
#####

import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1) 

if rank == 1:
#         randNum = numpy.random.random_sample(1)
        randNum = numpy.array([50], dtype=numpy.float64)
        print("Process", rank, "drew the number", randNum[0])
        
        req1 = comm.Isend(randNum, dest=0)
        req1.Wait()
        
        randNum[0] /= 10 # overlap communication
        print("Process", rank, "number in overlap communication =", randNum[0])
        
        req = comm.Irecv(randNum, source=0)
        req.Wait()
        print("Process", rank, "received the number", randNum[0])

if rank == 0:
        print("Process", rank, "before receiving has the number", randNum[0])
        req1 = comm.Irecv(randNum, source=1)
        req1.Wait()
        print("Process", rank, "received the number", randNum[0])
        randNum *= 2
        req = comm.Isend(randNum, dest=1)
