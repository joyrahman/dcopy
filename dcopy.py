import sys
import scipy.linalg.blas as blas
import numpy as np
import os 


c_size = int(os.getenv('cache_size','20480'))
t = int(os.getenv('iteration','1000'))

#c_size = int(sys.argv[1])   #cache size
#t = int(sys.argv[2])        #number of loops


size = c_size*1000/8

a = [0] * size
b = [1] * size
c = np.array(a)
d = np.array(b)

for i in xrange(0,t):
    e = blas.dcopy(c,d)
    print "iter:{}, cache_size:{}".format(i, e.nbytes)
    d = np.array(b)
 

