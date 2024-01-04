import math
import numpy as np
import matplotlib.pyplot as plt
X = [[1,1],
     [1,-1],
     [-1,1],
     [-1,-1]
     ]
T = [-1,
     1,
     1,
     -1]
W = [0.5,0.3,0.7,0.1,0.4,0.9]

U = [0.8,0.2,0.6]
n = 0.65
itera = -1
maxitera = 1000
minError = 0.1
Emc = 10000000
ejex = np.arange(0,maxitera+1)
ejey0 = np.array([])
ejey1 = np.array([])
ejey2 = np.array([])
ejey3 = np.array([])
ejey4 = np.array([])
ejey5 = np.array([])
ejeyEmc = np.array([])

def f(x):
    return 1/(1+math.exp(-x))
def fprima(x):
    return f(x)*(1-f(x))
#inicia el proceso de aprendizaje de la red neuronal
while itera<maxitera and Emc >minError:
    itera = itera + 1
    Error = [0.0,0.0,0.0,0.0]
    for p in range(4):
        neta0 = X[p][0]*W[0] + X[p][1]*W[2] - U[0]
        neta1 = X[p][0]*W[1] + X[p][1]*W[3] - U[1]
        fneta0 = f(neta0)
        fneta1 = f(neta1)
        neta2 = fneta0*W[4] + fneta1*W[5] - U[2]
        fneta2 = f(neta2)# salida obtenida
        landa2 = (T[p] - fneta2)*fprima(neta2)
        landa1 = fprima(neta1)*landa2*W[5]
        landa0 = fprima(neta0)*landa2*W[4]
        # actualizar los pesos sinapticos
        # los pesos de la capa salida
        W[5] = W[5] +n*landa2*fneta1
        W[4] = W[4] +n*landa2*fneta0
        # actualiza los pesos de la capa oculta
        W[0] = W[0] + n*landa0*X[p][0]
        W[1] = W[1] + n*landa1*X[p][0]
        W[2] = W[2] + n*landa0*X[p][1]
        W[3] = W[3] + n*landa1*X[p][1]
        # actualizar los umbrales
        U[2] = U[2] + n*landa2*-1
        U[1] = U[1] + n*landa1*-1
        U[0] = U[0] + n*landa0*-1
        Error[p] = 0.5*(T[p] - fneta2)*(T[p] - fneta2)

    ejey0 = np.insert(ejey0,ejey0.size,W[0])
    ejey1 = np.insert(ejey1,ejey1.size,W[1])
    ejey2 = np.insert(ejey2,ejey2.size,W[2])
    ejey3 = np.insert(ejey3,ejey3.size,W[3])
    ejey4 = np.insert(ejey4,ejey4.size,W[4])
    ejey5 = np.insert(ejey5,ejey5.size,W[5])       

    Emc = Error[0] + Error[1] + Error[2] + Error[3]
    ejeyEmc = np.insert(ejeyEmc,ejeyEmc.size,Emc)  
    print(itera," Error medio cuadratico: ",Emc)

print("Pesos sinapticos aprendidos")
print(W)
print(U)

def valor(x):
    if x>0.5:
        return 1
    else:
        return -1
    
print("Mapeo o comprobacion del aprendizaje de la red")
for i in range(4):
    neta0 = X[i][0]*W[0] + X[i][1]*W[2] - U[0]
    neta1 = X[i][0]*W[1] + X[i][1]*W[3] - U[1]
    fneta0 = f(neta0)
    fneta1 = f(neta1)
    neta2 = fneta0*W[4] + fneta1*W[5] - U[2]
    fneta2 = f(neta2)
    print(fneta2, "==>",valor(fneta2))

fig, (pesos,error) = plt.subplots(2,1)
pesos.plot(ejex, ejey0, '.-', label='W0')
pesos.plot(ejex, ejey1, '.-', label='W1')
pesos.plot(ejex, ejey2, '.-', label='W2')
pesos.plot(ejex, ejey3, '.-', label='W3')
pesos.plot(ejex, ejey4, '.-', label='W4')
pesos.plot(ejex, ejey5, '.-', label='W5')

legend = pesos.legend(loc='upper center',bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=6)

error.plot(ejex,ejeyEmc,'.-', label='Emc')
error.set_ylabel('Emc')
error.set_xlabel('Iteraciones')
plt.show()








