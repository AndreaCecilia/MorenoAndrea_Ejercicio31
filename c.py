import numpy as np
import matplotlib.pyplot as plt

#Iteracion = np.loadtxt('dataI.dat')
#errorcentro=np.loadtxt('dataE.dat')
#errorcon=np.loadtxt('dataC.dat')


plt.figure(figsize=(14,4))
    
plt.subplot(1,3,1)
   # plt.plot(Iteracion[:,0],Iteracion[:,1], , 'bo')
plt.ylabel("N iteraciones")
plt.xlabel("N_x")

plt.subplot(1,3,2)

    #plt.plot(errorcentro[:,0],errorcentro[:,1], , 'bo')
plt.ylabel("Error centro x 10↨^2")
plt.xlabel("N_x")

plt.subplot(1,3,3)
    #plt.plot(errorcon[:,0],errorcon[:,1], , 'bo')
plt.ylabel("Error convergencia x 10↨^6")
plt.xlabel("N_x")

plt.savefig("rta.png")

