import math
import numpy as np
import matplotlib.pyplot as plt
import random


X = [[1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 0, 1]
    ]

T = [[0, 0],
     [0, 0],
     [0, 1],
     [0, 1],
     [0, 1],
     [1, 0],
     [1, 0],
     [1, 0],
     [1, 1],
     [1, 1],
     [1, 1],
     [1, 0],
     [0, 0],
     [0, 0],
     [1, 0],
     [0, 1],
     [1, 1],
     [0, 0],
     [0, 1],
     [0, 1]]

W = [random.randint(0, 1) for _ in range(80)]

U = [random.randint(0, 1) for _ in range(10)]

n = 0.65
itera = -1
maxitera = 2000
minError = 0.1
Emc = 10000000

errors = []

delta8 = np.zeros(9)
delta9 = np.zeros(9)

def f(x):
    return 1/(1+math.exp(-x))
def fprima(x):
    return f(x)*(1-f(x))
#inicia el proceso de aprendizaje de la red neuronal
while itera<maxitera and Emc >minError:
    itera = itera + 1
    Error = np.zeros((len(X), 2))
    for p in range(4):
        neta0 = X[p][0]*W[0] + X[p][1]*W[8] + X[p][2]*W[16] + X[p][3]*W[24] + X[p][4]*W[32] + X[p][5]*W[40] + X[p][6]*W[48] + X[p][7]*W[56]- U[0]
        neta1 = X[p][0]*W[1] + X[p][1]*W[9] + X[p][2]*W[17] + X[p][3]*W[25] + X[p][4]*W[33] + X[p][5]*W[41] + X[p][6]*W[40] + X[p][7]*W[57]- U[1]
        neta2 = X[p][0]*W[2] + X[p][1]*W[10] + X[p][2]*W[18] + X[p][3]*W[26] + X[p][4]*W[34] + X[p][5]*W[42] + X[p][6]*W[50] + X[p][7]*W[58] - U[2]
        neta3 = X[p][0]*W[3] + X[p][1]*W[11] + X[p][2]*W[19] + X[p][3]*W[27] + X[p][4]*W[35] + X[p][5]*W[43] + X[p][6]*W[51] + X[p][7]*W[59] - U[3]
        neta4 = X[p][0]*W[4] + X[p][1]*W[12] + X[p][2]*W[20] + X[p][3]*W[28] + X[p][4]*W[36] + X[p][5]*W[44] + X[p][6]*W[52] + X[p][7]*W[61] - U[4]
        neta5 = X[p][0]*W[5] + X[p][1]*W[13] + X[p][2]*W[21] + X[p][3]*W[29] + X[p][4]*W[37] + X[p][5]*W[45] + X[p][6]*W[53] + X[p][7]*W[61] - U[5]
        neta6 = X[p][0]*W[6] + X[p][1]*W[14] + X[p][2]*W[22] + X[p][3]*W[30] + X[p][4]*W[38] + X[p][5]*W[46] + X[p][6]*W[54] + X[p][7]*W[62] - U[6]
        neta7 = X[p][0]*W[7] + X[p][1]*W[15] + X[p][2]*W[23] + X[p][3]*W[31] + X[p][4]*W[39] + X[p][5]*W[47] + X[p][6]*W[55] + X[p][7]*W[63] - U[7]

        fneta0 = f(neta0)
        fneta1 = f(neta1)
        fneta2 = f(neta2)
        fneta3 = f(neta3)
        fneta4 = f(neta4)
        fneta5 = f(neta5)
        fneta6 = f(neta6)
        fneta7 = f(neta7)

        neta8 = fneta0*W[64] + fneta1*W[66] + fneta2*W[68]+ fneta3*W[70] + fneta4*W[72] + fneta5*W[74] + fneta6*W[76] + fneta7*W[78] - U[8]
        neta9 = fneta0*W[65] + fneta1*W[67] + fneta2*W[69]+ fneta3*W[71] + fneta4*W[73] + fneta5*W[75] + fneta6*W[77] + fneta7*W[79] - U[9]
        fneta8 = f(neta8)
        fneta9 = f(neta9)

        delta8[0] = (T[p][0] - fneta8)*fprima(neta8)
        delta8[1] = fprima(neta0)*delta8[0]*W[64]
        delta8[2] = fprima(neta1)*delta8[0]*W[66]
        delta8[3] = fprima(neta2)*delta8[0]*W[68]
        delta8[4] = fprima(neta3)*delta8[0]*W[70]
        delta8[5] = fprima(neta4)*delta8[0]*W[72]
        delta8[6] = fprima(neta5)*delta8[0]*W[74]
        delta8[7] = fprima(neta6)*delta8[0]*W[76]
        delta8[8] = fprima(neta7)*delta8[0]*W[78]

        delta9[0] = (T[p][1] - fneta9)*fprima(neta9)
        delta9[1] = fprima(neta0)*delta9[0]*W[65]
        delta9[2] = fprima(neta1)*delta9[0]*W[67]
        delta9[3] = fprima(neta2)*delta9[0]*W[69]
        delta9[4] = fprima(neta3)*delta9[0]*W[71]
        delta9[5] = fprima(neta4)*delta9[0]*W[73]
        delta9[6] = fprima(neta5)*delta9[0]*W[75]
        delta9[7] = fprima(neta6)*delta9[0]*W[77]
        delta9[8] = fprima(neta7)*delta9[0]*W[79]

        # actualizar los pesos sinapticos
        # los pesos de la capa salida
        W[64] += n * delta8[0] * fneta0
        W[66] += n * delta8[0] * fneta1
        W[68] += n * delta8[0] * fneta2
        W[70] += n * delta8[0] * fneta3
        W[72] += n * delta8[0] * fneta4
        W[74] += n * delta8[0] * fneta5
        W[76] += n * delta8[0] * fneta6
        W[78] += n * delta8[0] * fneta7

        W[65] += n * delta9[0] * fneta0
        W[67] += n * delta9[0] * fneta1
        W[69] += n * delta9[0] * fneta2
        W[71] += n * delta9[0] * fneta3
        W[73] += n * delta9[0] * fneta4
        W[75] += n * delta9[0] * fneta5
        W[77] += n * delta9[0] * fneta6
        W[79] += n * delta9[0] * fneta7


        W[0] += n * delta8[1] * X[p][0] + n * delta9[1] * X[p][0]
        W[8] += n * delta8[1] * X[p][1] + n * delta9[1] * X[p][1]
        W[16] += n * delta8[1] * X[p][2] + n * delta9[1] * X[p][2]
        W[24] += n * delta8[1] * X[p][3] + n * delta9[1] * X[p][3]
        W[32] += n * delta8[1] * X[p][4] + n * delta9[1] * X[p][4]
        W[40] += n * delta8[1] * X[p][5] + n * delta9[1] * X[p][5]
        W[48] += n * delta8[1] * X[p][6] + n * delta9[1] * X[p][6]
        W[56] += n * delta8[1] * X[p][7] + n * delta9[1] * X[p][7]

        W[1] += n * delta8[2] * X[p][0] + n * delta9[2] * X[p][0]
        W[9] += n * delta8[2] * X[p][1] + n * delta9[2] * X[p][1]
        W[17] += n * delta8[2] * X[p][2] + n * delta9[2] * X[p][2]
        W[25] += n * delta8[2] * X[p][3] + n * delta9[2] * X[p][3]
        W[33] += n * delta8[2] * X[p][4] + n * delta9[2] * X[p][4]
        W[41] += n * delta8[2] * X[p][5] + n * delta9[2] * X[p][5]
        W[49] += n * delta8[2] * X[p][6] + n * delta9[2] * X[p][6]
        W[57] += n * delta8[2] * X[p][7] + n * delta9[2] * X[p][7]

        W[2] += n * delta8[3] * X[p][0] + n * delta9[3] * X[p][0]
        W[10] += n * delta8[3] * X[p][1] + n * delta9[3] * X[p][1]
        W[18] += n * delta8[3] * X[p][2] + n * delta9[3] * X[p][2]
        W[26] += n * delta8[3] * X[p][3] + n * delta9[3] * X[p][3]
        W[34] += n * delta8[3] * X[p][4] + n * delta9[3] * X[p][4]
        W[42] += n * delta8[3] * X[p][5] + n * delta9[3] * X[p][5]
        W[50] += n * delta8[3] * X[p][6] + n * delta9[3] * X[p][6]
        W[58] += n * delta8[3] * X[p][7] + n * delta9[3] * X[p][7]

        W[3] += n * delta8[4] * X[p][0] + n * delta9[4] * X[p][0]
        W[11] += n * delta8[4] * X[p][1] + n * delta9[4] * X[p][1]
        W[19] += n * delta8[4] * X[p][2] + n * delta9[4] * X[p][2]
        W[27] += n * delta8[4] * X[p][3] + n * delta9[4] * X[p][3]
        W[35] += n * delta8[4] * X[p][4] + n * delta9[4] * X[p][4]
        W[43] += n * delta8[4] * X[p][5] + n * delta9[4] * X[p][5]
        W[51] += n * delta8[4] * X[p][6] + n * delta9[4] * X[p][6]
        W[59] += n * delta8[4] * X[p][7] + n * delta9[4] * X[p][7]

        W[4] += n * delta8[5] * X[p][0] + n * delta9[5] * X[p][0]
        W[12] += n * delta8[5] * X[p][1] + n * delta9[5] * X[p][1]
        W[20] += n * delta8[5] * X[p][2] + n * delta9[5] * X[p][2]
        W[28] += n * delta8[5] * X[p][3] + n * delta9[5] * X[p][3]
        W[36] += n * delta8[5] * X[p][4] + n * delta9[5] * X[p][4]
        W[44] += n * delta8[5] * X[p][5] + n * delta9[5] * X[p][5]
        W[52] += n * delta8[5] * X[p][6] + n * delta9[5] * X[p][6]
        W[60] += n * delta8[5] * X[p][7] + n * delta9[5] * X[p][7]

        W[5] += n * delta8[6] * X[p][0] + n * delta9[6] * X[p][0]
        W[13] += n * delta8[6] * X[p][1] + n * delta9[6] * X[p][1]
        W[21] += n * delta8[6] * X[p][2] + n * delta9[6] * X[p][2]
        W[29] += n * delta8[6] * X[p][3] + n * delta9[6] * X[p][3]
        W[37] += n * delta8[6] * X[p][4] + n * delta9[6] * X[p][4]
        W[45] += n * delta8[6] * X[p][5] + n * delta9[6] * X[p][5]
        W[53] += n * delta8[6] * X[p][6] + n * delta9[6] * X[p][6]
        W[61] += n * delta8[6] * X[p][7] + n * delta9[6] * X[p][7]

        W[6] += n * delta8[7] * X[p][0] + n * delta9[7] * X[p][0]
        W[14] += n * delta8[7] * X[p][1] + n * delta9[7] * X[p][1]
        W[22] += n * delta8[7] * X[p][2] + n * delta9[7] * X[p][2]
        W[30] += n * delta8[7] * X[p][3] + n * delta9[7] * X[p][3]
        W[38] += n * delta8[7] * X[p][4] + n * delta9[7] * X[p][4]
        W[46] += n * delta8[7] * X[p][5] + n * delta9[7] * X[p][5]
        W[54] += n * delta8[7] * X[p][6] + n * delta9[7] * X[p][6]
        W[62] += n * delta8[7] * X[p][7] + n * delta9[7] * X[p][7]
        
        W[7] += n * delta8[8] * X[p][0] + n * delta9[8] * X[p][0]
        W[15] += n * delta8[8] * X[p][1] + n * delta9[8] * X[p][1]
        W[23] += n * delta8[8] * X[p][2] + n * delta9[8] * X[p][2]
        W[31] += n * delta8[8] * X[p][3] + n * delta9[8] * X[p][3]
        W[39] += n * delta8[8] * X[p][4] + n * delta9[8] * X[p][4]
        W[47] += n * delta8[8] * X[p][5] + n * delta9[8] * X[p][5]
        W[55] += n * delta8[8] * X[p][6] + n * delta9[8] * X[p][6]
        W[63] += n * delta8[8] * X[p][7] + n * delta9[8] * X[p][7]

        U[9] += n * delta9[0] * -1
        U[8] += n * delta8[0] * -1
        U[7] += n * delta8[8] * -1 + n * delta9[8] * -1
        U[6] += n * delta8[7] * -1 + n * delta9[7] * -1
        U[5] += n * delta8[6] * -1 + n * delta9[6] * -1
        U[4] += n * delta8[5] * -1 + n * delta9[5] * -1
        U[3] += n * delta8[4] * -1 + n * delta9[4] * -1
        U[2] += n * delta8[3] * -1 + n * delta9[3] * -1
        U[1] += n * delta8[2] * -1 + n * delta9[2] * -1
        U[0] += n * delta8[1] * -1 + n * delta9[1] * -1

        Error[p][0] = 0.5 * (T[p][0] - fneta8) ** 2
        Error[p][1] = 0.5 * (T[p][1] - fneta9) ** 2

    sum_squared_errors = np.sum(Error ** 2)
    num_samples = len(X)
    Emc = np.sqrt(sum_squared_errors / (2*num_samples))
    #errors.append(Emc)
    #ejeyEmc = np.insert(ejeyEmc,ejeyEmc.size,Emc)  
    print(itera," Error medio cuadratico: ",Emc)

print("Pesos sinapticos aprendidos")
print(W)
print(U)

def valor(x):
    if x>0.5:
        return 1
    else:
        return 0
def E(y1,y2):
    if y1==0 and y2==0:
        return 0
    elif y1==0 and y2==1:
        return 1
    elif y1==1 and y2==0:
        return 2
    else:
        return 3

print("Mapeo o comprobacion del aprendizaje de la red")
for i in range(4):
    neta0 = X[p][0]*W[0] + X[p][1]*W[8] + X[p][2]*W[16] + X[p][3]*W[24] + X[p][4]*W[32] + X[p][5]*W[40] + X[p][6]*W[48] + X[p][7]*W[56]- U[0]
    neta1 = X[p][0]*W[1] + X[p][1]*W[9] + X[p][2]*W[17] + X[p][3]*W[25] + X[p][4]*W[33] + X[p][5]*W[41] + X[p][6]*W[40] + X[p][7]*W[57]- U[1]
    neta2 = X[p][0]*W[2] + X[p][1]*W[10] + X[p][2]*W[18] + X[p][3]*W[26] + X[p][4]*W[34] + X[p][5]*W[42] + X[p][6]*W[50] + X[p][7]*W[58] - U[2]
    neta3 = X[p][0]*W[3] + X[p][1]*W[11] + X[p][2]*W[19] + X[p][3]*W[27] + X[p][4]*W[35] + X[p][5]*W[43] + X[p][6]*W[51] + X[p][7]*W[59] - U[3]
    neta4 = X[p][0]*W[4] + X[p][1]*W[12] + X[p][2]*W[20] + X[p][3]*W[28] + X[p][4]*W[36] + X[p][5]*W[44] + X[p][6]*W[52] + X[p][7]*W[61] - U[4]
    neta5 = X[p][0]*W[5] + X[p][1]*W[13] + X[p][2]*W[21] + X[p][3]*W[29] + X[p][4]*W[37] + X[p][5]*W[45] + X[p][6]*W[53] + X[p][7]*W[61] - U[5]
    neta6 = X[p][0]*W[6] + X[p][1]*W[14] + X[p][2]*W[22] + X[p][3]*W[30] + X[p][4]*W[38] + X[p][5]*W[46] + X[p][6]*W[54] + X[p][7]*W[62] - U[6]
    neta7 = X[p][0]*W[7] + X[p][1]*W[15] + X[p][2]*W[23] + X[p][3]*W[31] + X[p][4]*W[39] + X[p][5]*W[47] + X[p][6]*W[55] + X[p][7]*W[63] - U[7]
    
    fneta0 = f(neta0)
    fneta1 = f(neta1)
    fneta2 = f(neta2)
    fneta3 = f(neta3)
    fneta4 = f(neta4)
    fneta5 = f(neta5)
    fneta6 = f(neta6)
    fneta7 = f(neta7)
    
    neta8 = fneta0*W[64] + fneta1*W[66] + fneta2*W[68]+ fneta3*W[70] + fneta4*W[72] + fneta5*W[74] + fneta6*W[76] + fneta7*W[78] - U[8]
    neta9 = fneta0*W[65] + fneta1*W[67] + fneta2*W[69]+ fneta3*W[71] + fneta4*W[73] + fneta5*W[75] + fneta6*W[77] + fneta7*W[79] - U[9]
    fneta8 = f(neta8)
    fneta9 = f(neta9)

    print("Entrada: ", X[i], " Salida obtenida: ", fneta8, " ", fneta9, " Evaluando por la funcion valor: ", valor(fneta8), valor(fneta9)," Enfermedad",E(valor(fneta8), valor(fneta9)))

#1 1 1 1 0 1 0 1 ?0 ?1 ?

print("***************************************")


neta0 = 1*W[0] + 1*W[8] + 1*W[16] + 1*W[24] + 0*W[32] + 1*W[40] + 0*W[48] + 1*W[56]- U[0]
neta1 = 1*W[1] + 1*W[9] + 1*W[17] + 1*W[25] + 0*W[33] + 1*W[41] + 0*W[40] + 1*W[57]- U[1]
neta2 = 1*W[2] + 1*W[10] + 1*W[18] + 1*W[26] + 0*W[34] + 1*W[42] + 0*W[50] + 1*W[58] - U[2]
neta3 = 1*W[3] + 1*W[11] + 1*W[19] + 1*W[27] + 0*W[35] + 1*W[43] + 0*W[51] + 1*W[59] - U[3]
neta4 = 1*W[4] + 1*W[12] + 1*W[20] + 1*W[28] + 0*W[36] + 1*W[44] + 0*W[52] + 1*W[61] - U[4]
neta5 = 1*W[5] + 1*W[13] + 1*W[21] + 1*W[29] + 0*W[37] + 1*W[45] + 0*W[53] + 1*W[61] - U[5]
neta6 = 1*W[6] + 1*W[14] + 1*W[22] + 1*W[30] + 0*W[38] + 1*W[46] + 0*W[54] + 1*W[62] - U[6]
neta7 = 1*W[7] + 1*W[15] + 1*W[23] + 1*W[31] + 0*W[39] + 1*W[47] + 0*W[55] + 1*W[63] - U[7]

fneta0 = f(neta0)
fneta1 = f(neta1)
fneta2 = f(neta2)
fneta3 = f(neta3)
fneta4 = f(neta4)
fneta5 = f(neta5)
fneta6 = f(neta6)
fneta7 = f(neta7)
    
neta8 = fneta0*W[64] + fneta1*W[66] + fneta2*W[68]+ fneta3*W[70] + fneta4*W[72] + fneta5*W[74] + fneta6*W[76] + fneta7*W[78] - U[8]
neta9 = fneta0*W[65] + fneta1*W[67] + fneta2*W[69]+ fneta3*W[71] + fneta4*W[73] + fneta5*W[75] + fneta6*W[77] + fneta7*W[79] - U[9]
fneta8 = f(neta8)
fneta9 = f(neta9)
y1 = valor(fneta8)
y2 = valor(fneta9)
print(f"\nCaso de comprobacion: 1 1 1 1 0 1 0 1, Y1= 0, Y2 = 1, E=?")
print(f"Entrada: 1 1 1 1 0 1 0 1 Salida obtenida: Y1={y1} Y2={y2} Enfermedad: {E(y1,y2)}")
print("\n***************************************")

