import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('bmh')


l = 3 #ancho grilla para primer caso

x = np.linspace(-l, l, 25) #puntos de la grilla
z = np.linspace(-l, l, 25)

X, Z = np.meshgrid(x,z) #definimos la grilla


#A continuación se definen las componentes x y z del campo magnético, para r<a y r>a, B1 y B2
#respectivamente. Notemos que hemos impuesto que mu_0*I/2 = 1 y a = 1. Además, se define la norma del vector
#(x,z) que es útil para los cálculos.


def B1_x(x,z):
    return 1.5*x*z

def B1_z(z):
    return -1.5*(z)**2 + 1

def r(x,z):
    return np.sqrt(x**2 + z**2)

def B2_x(x,z):
    return (1.5*x*z)/r(x,z)**5 + (45/8)*(x*z/(r(x,z)**7)) - (105/8)*(((z**3)*x)/(r(x,z))**9)

def B2_z(x,z):
    return -0.5/(r(x,z)**3) - (1/8)*(9-24*z**2)/(r(x,z)**5) + (27/4)*z**2/(r(x,z)**7) - (15/8)*z**4/(r(x,z)**9)

def B1(x,z):
    return np.sqrt(B1_x(x,z)**2 + B1_z(z)**2)

def B2(x,z):
    return np.sqrt(B2_x(x,z)**2 + B2_z(x,z)**2)


for i in range(len(x)): #se grafica caso a caso para distinguir el campo para r<a y r>a
    for j in range(len(z)):
        if x[i]**2 + z[j]**2 < 1:
            plt.quiver(X[i,j], Z[i,j], B1_x(X[i,j],Z[i,j])/B1(X[i,j],Z[i,j]), B1_z(Z[i,j])/B1(X[i,j],Z[i,j]), np.log(B1(X[i,j],Z[i,j])), pivot='middle', scale=30)
        else:
            plt.quiver(X[i,j], Z[i,j], B2_x(X[i,j],Z[i,j])/B2(X[i,j],Z[i,j]), B2_z(X[i,j],Z[i,j])/B2(X[i,j],Z[i,j]), np.log(B2(X[i,j],Z[i,j])), pivot='middle', scale=30)

plt.title(r'$\vec{B}(x,z)$')
plt.xlabel('$x$')
plt.ylabel('$z$')

plt.savefig('B.pdf')

plt.show()

