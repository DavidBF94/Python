from matplotlib.pyplot import plot,show
from random import randrange,random
from numpy import arange

Probab_1=97.91*100
Probab_2=2.09*100

Tmax=20000
h=1
t=arange(0.0,Tmax,h)

Tau_213Bi=46*60
Tau_209Pb=3.3*60
Tau_209Tl=2.2*60

P_213Bi=1-2**(-h/Tau_213Bi)
P_209Pb=1-2**(-h/Tau_209Pb)
P_209Tl=1-2**(-h/Tau_209Tl)

###########################################################

N_213Bi=10000
N_209Pb=0
N_209Tl=0
N_209Bi=0

Puntos_213Bi=[]
Puntos_209Pb=[]
Puntos_209Tl=[]
Puntos_209Bi=[]

for i in t:
    Puntos_213Bi.append(N_213Bi)
    Puntos_209Pb.append(N_209Pb)
    Puntos_209Tl.append(N_209Tl)
    Puntos_209Bi.append(N_209Bi)
    
    Dec_213Bi=0
    Dec_209Pb=0
    Dec_209Tl=0
    
    for j in range(N_213Bi):
        if random()<P_213Bi:
            Dec_213Bi+=1
            N_213Bi-=Dec_213Bi
            if randrange(0,10001)<Probab_1:
                if random()<P_209Pb:
                    Dec_209Pb+=1
                    N_209Pb+=Dec_213Bi-Dec_209Pb
                    N_209Bi+=Dec_209Pb
                else:
                    N_209Pb+=Dec_213Bi
            else:
                if random()<P_209Tl:
                    Dec_209Tl+=1
                    N_209Tl+=Dec_213Bi-Dec_209Tl
                    if random()<P_209Pb:
                        Dec_209Pb+=1
                        N_209Pb+=Dec_209Tl-Dec_209Pb
                        N_209Bi+=Dec_209Pb
                    else:
                        N_209Pb+=Dec_209Tl
                else:
                    N_209Tl+=Dec_213Bi
    
plot(t,Puntos_213Bi)
plot(t,Puntos_209Pb)
plot(t,Puntos_209Tl)
plot(t,Puntos_209Bi)
show()

print("Los Isótopos finales de 213Bi son: ",N_213Bi)
print("Los Isótopos finales de 209Pb son: ",N_209Pb)
print("Los Isótopos finales de 209Tl son: ",N_209Tl)
print("Los Isótopos finales de 209Bi son: ",N_209Bi)