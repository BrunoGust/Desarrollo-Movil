import random
class Neurona:
    e = 0.5
    w0 = random.random()
    w1 = random.random()
    u = random.random()
    def __init__(self):
        print("creado")
    def entradas(self,X):
        x0,x1 = X[0],X[1]
        # Formula 1
        y = x0*self.w0 + x1*self.w1 + (-1)*self.u
        # Formula 2
        Y = -1
        if y>=0:
            Y = 1
        return Y
    def actualizar(self,Ti,X):
        # Formula 3
        x0,x1 = X[0],X[1]
        self.w0 = self.w0  + 2*0.5*Ti*x0
        self.w1 = self.w1  + 2*0.5*Ti*x1
        self.u = self.u  + 2*0.5*Ti*(-1)
        return self.w0,self.w1,self.u
    
X = [[1.0,1.0],
     [1.0,-1.0],
     [-1.0,1.0],
     [-1.0,-1.0]
     ]
T = [1.0,
     1.0,
     1.0,
     -1.0]

i = 0
n = Neurona()
while i<4:
    y = n.entradas(X[i])
    if y!=T[i]:
        w0,w1,u = n.actualizar(T[i],X[i])
        print(w0,w1,u)
        i = -1
    i = i +1
    
# Mapeo
for i in range(4):
    y = n.entradas(X[i])
    print(X[i],y)
