import math
import numpy as np
import matplotlib.pyplot as plt
X = [[1, 1, 1, 1],
     [1, -1, -1, 1],
     [-1, 1, 1, 1],
     [-1, -1, -1, 1]
     ]

T = [[1, -1],
     [-1, 1],
     [1,-1],
     [-1,1]]

W = [0.5, 0.3, 0.7, #x0
    0.1, 0.4, 0.9,  #x1
    0.8, 0.9, 0.5,  #x2
    0.4, 0.7, 0.9,  #x3
    0.4, 0.7,       #0
    0.9, 0.8,       #1
    0.7, 0.6]       #2

U = [0.8,0.2,0.6,
    0.9,0.8]

n = 0.65
itera = -1
maxitera = 2500
minError = 0.1
Emc = 10000000

errors = []

delta3 = np.zeros(4)
delta4 = np.zeros(4)

ejex = np.arange(0,maxitera+1)
ejey0 = np.array([])
ejey1 = np.array([])
ejey2 = np.array([])
ejey3 = np.array([])
ejey4 = np.array([])
ejey5 = np.array([])
ejey6 = np.array([])
ejey7 = np.array([])
ejey8 = np.array([])
ejey9 = np.array([])
ejey10 = np.array([])
ejey11 = np.array([])
ejey12 = np.array([])
ejey13 = np.array([])
ejey14 = np.array([])
ejey15 = np.array([])
ejey16 = np.array([])
ejey17 = np.array([])

ejeyEmc = np.array([])

def f(x):
    return 1/(1+math.exp(-x))
def fprima(x):
    return f(x)*(1-f(x))
#inicia el proceso de aprendizaje de la red neuronal
while itera<maxitera and Emc >minError:
    itera = itera + 1
    Error = np.zeros((len(X), 2))
    for p in range(4):
        neta0 = X[p][0]*W[0] + X[p][1]*W[3] + X[p][2]*W[6] + X[p][3]*W[9]- U[0]
        neta1 = X[p][0]*W[1] + X[p][1]*W[4] + X[p][2]*W[7] + X[p][3]*W[10]- U[1]
        neta2 = X[p][0]*W[2] + X[p][1]*W[5] + X[p][2]*W[8] + X[p][3]*W[11]- U[2]
        fneta0 = f(neta0)
        fneta1 = f(neta1)
        fneta2 = f(neta2)

        neta3 = fneta0*W[12] + fneta1*W[14] + fneta2*W[16]- U[3]
        neta4 = fneta0*W[13] + fneta1*W[15] + fneta2*W[17]- U[4]
        fneta3 = f(neta3)
        fneta4 = f(neta4)

        delta3[0] = (T[p][0] - fneta3) * fprima(neta3)
        delta3[1] = fprima(neta0) * delta3[0] * W[12]
        delta3[2] = fprima(neta1) * delta3[0] * W[14]
        delta3[3] = fprima(neta2) * delta3[0] * W[16]

        delta4[0] = (T[p][1] - fneta4) * fprima(neta4)
        delta4[1] = fprima(neta0) * delta4[0] * W[13]
        delta4[2] = fprima(neta1) * delta4[0] * W[15]
        delta4[3] = fprima(neta2) * delta4[0] * W[17]

        # actualizar los pesos sinapticos
        # los pesos de la capa salida
        W[12] += n * delta3[0] * fneta0
        W[14] += n * delta3[0] * fneta1
        W[16] += n * delta3[0] * fneta2

        W[13] += n * delta4[0] * fneta0
        W[15] += n * delta4[0] * fneta1
        W[17] += n * delta4[0] * fneta2

        W[0] += n * delta3[1] * X[p][0] + n * delta4[1] * X[p][0]
        W[3] += n * delta3[1] * X[p][1] + n * delta4[1] * X[p][1]
        W[6] += n * delta3[1] * X[p][2] + n * delta4[1] * X[p][2]
        W[9] += n * delta3[1] * X[p][3] + n * delta4[1] * X[p][3]

        W[1] += n * delta3[2] * X[p][0] + n * delta4[2] * X[p][0]
        W[4] += n * delta3[2] * X[p][1] + n * delta4[2] * X[p][1]
        W[7] += n * delta3[2] * X[p][2] + n * delta4[2] * X[p][2]
        W[10] += n * delta3[2] * X[p][3] + n * delta4[2] * X[p][3]

        W[2] += n * delta3[3] * X[p][0] + n * delta4[3] * X[p][0]
        W[5] += n * delta3[3] * X[p][1] + n * delta4[3] * X[p][1]
        W[8] += n * delta3[3] * X[p][2] + n * delta4[3] * X[p][2]
        W[11] += n * delta3[3] * X[p][3] + n * delta4[3] * X[p][3]

        U[4] += n * delta4[0] * -1
        U[3] += n * delta3[0] * -1
        U[2] += n * delta3[3] * -1 + n * delta4[3] * -1
        U[1] += n * delta3[2] * -1 + n * delta4[2] * -1
        U[0] += n * delta3[1] * -1 + n * delta4[1] * -1

        Error[p][0] = 0.5 * (T[p][0] - fneta3) ** 2
        Error[p][1] = 0.5 * (T[p][1] - fneta4) ** 2

    ejey0 = np.insert(ejey0,ejey0.size,W[0])
    ejey1 = np.insert(ejey1,ejey1.size,W[1])
    ejey2 = np.insert(ejey2,ejey2.size,W[2])
    ejey3 = np.insert(ejey3,ejey3.size,W[3])
    ejey4 = np.insert(ejey4,ejey4.size,W[4])
    ejey5 = np.insert(ejey5,ejey5.size,W[5])
    ejey6 = np.insert(ejey6,ejey6.size,W[6])
    ejey7 = np.insert(ejey7,ejey7.size,W[7])
    ejey8 = np.insert(ejey8,ejey8.size,W[8])
    ejey9 = np.insert(ejey9,ejey9.size,W[9])
    ejey10 = np.insert(ejey10,ejey10.size,W[10])
    ejey11 = np.insert(ejey11,ejey11.size,W[11])    
    ejey12 = np.insert(ejey12,ejey12.size,W[12])
    ejey13 = np.insert(ejey13,ejey13.size,W[13])
    ejey14 = np.insert(ejey14,ejey14.size,W[14])
    ejey15 = np.insert(ejey15,ejey15.size,W[15])
    ejey16 = np.insert(ejey16,ejey16.size,W[16])
    ejey17 = np.insert(ejey17,ejey17.size,W[17])      

    sum_squared_errors = np.sum(Error ** 2)
    num_samples = len(X)
    Emc = np.sqrt(sum_squared_errors / (2*num_samples))
    errors.append(Emc)
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
    neta0 = X[i][0] * W[0] + X[i][1] * W[3] + X[i][2] * W[6] + X[i][3] * W[9] - U[0]
    neta1 = X[i][0] * W[1] + X[i][1] * W[4] + X[i][2] * W[7] + X[i][3] * W[10] - U[1]
    neta2 = X[i][0] * W[2] + X[i][1] * W[5] + X[i][2] * W[8] + X[i][3] * W[11] - U[2]
    fneta0 = f(neta0)
    fneta1 = f(neta1)
    fneta2 = f(neta2)
    neta3 = fneta0 * W[12] + fneta1 * W[14] + fneta2 * W[16] - U[3]
    neta4 = fneta0 * W[13] + fneta1 * W[15] + fneta2 * W[17] - U[4]
    fneta3 = f(neta3)
    fneta4 = f(neta4)
    print("Entrada: ", X[i], " Salida obtenida: ", fneta3, " ", fneta4, " Evaluando por la funcion valor: ", valor(fneta3), valor(fneta4))


fig, (pesos,error) = plt.subplots(2,1)
pesos.plot(ejex, ejey0, '.-', label='W0')
pesos.plot(ejex, ejey1, '.-', label='W1')
pesos.plot(ejex, ejey2, '.-', label='W2')
pesos.plot(ejex, ejey3, '.-', label='W3')
pesos.plot(ejex, ejey4, '.-', label='W4')
pesos.plot(ejex, ejey5, '.-', label='W5')
pesos.plot(ejex, ejey6, '.-', label='W6')
pesos.plot(ejex, ejey7, '.-', label='W7')
pesos.plot(ejex, ejey8, '.-', label='W8')
pesos.plot(ejex, ejey9, '.-', label='W9')
pesos.plot(ejex, ejey10, '.-', label='W10')
pesos.plot(ejex, ejey11, '.-', label='W11')
pesos.plot(ejex, ejey12, '.-', label='W12')
pesos.plot(ejex, ejey13, '.-', label='W13')
pesos.plot(ejex, ejey14, '.-', label='W14')
pesos.plot(ejex, ejey15, '.-', label='W15')
pesos.plot(ejex, ejey16, '.-', label='W16')
pesos.plot(ejex, ejey17, '.-', label='W17')


legend = pesos.legend(loc='upper center',bbox_to_anchor=(0.5, -0.05),fancybox=True, shadow=True, ncol=18)

error.plot(ejex,ejeyEmc,'.-', label='Emc')
error.set_ylabel('Emc')
error.set_xlabel('Iteraciones')
plt.show()








