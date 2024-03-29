import numpy as np 
import matplotlib.pyplot as plt
plt.style.use('bmh') 
from mpl_toolkits.mplot3d import Axes3D
import scipy as sp 

"""Ésta rutina contiene lo esencial para resolver
los últimos puntos de la primera pregunta
de la tarea 1, a excepción de la animación
de la trayectoria de q."""

def f(t, V): #V = [p,phi,z, dpdt, dphidt, dzdt]
    return [
        V[3], V[4], V[5], #la función devuelve las derivadas de las entradas de V
        V[0]*V[4]**2 - V[5]/V[0], (-2*V[3]*V[4])/V[0], V[3]/V[0]
    ]

t_inter = (0,10) #intervalo de tiempo de integración
t = np.linspace(*t_inter, 1000) #instantes a graficar en el intervalo

V0 = [1,0,0,0,1,0] #Primera condición inicial

V1 = [0.25,0,0.75,0,1,0] #Segunda condición inicial

V2 = [0.5, 0, 0.5, 0.5, 0.5, 0.5] #Tercera condición inicial

sol = sp.integrate.solve_ivp(f, t_inter, V2, t_eval=t) #solve_ivp calcula las entradas de V

rho = np.array(sol.y[0]) #Se recuperan los resultados para rho, phi y z adimensionados
phi = np.array(sol.y[1])
zeth = np.array(sol.y[2])

drho = np.array(sol.y[3]) #Se recuperan los resultados para drho/dt, dphi/dt y dz/dt adimensionados
dphi= np.array(sol.y[4])
dz = np.array(sol.y[5])

E = 0.5*(drho**2 + (rho**2)*dphi**2 + dz**2) #Esta es una energía adimensionalizada de la forma E* = E/m
                                             #considerando que utilizamos las velocidades adimensionadas

x = rho*np.cos(phi) #transformación a coordenadas cartesianas
y = rho*np.sin(phi)
z = zeth 

#ax = plt.axes(projection='3d')
#ax.plot3D(x, y, z, color='blue', label='Trayectoria')
#ax.set_xlabel(r'$\vec{x}(t)$')
#ax.set_ylabel(r'$\vec{y}(t)$')
#ax.set_zlabel(r'$\vec{z}(t)$')
#ax.set_title('Trayectoria de $q$ (3ra condición inicial)', fontsize=12)
#ax.view_init(elev=20., azim=-35, roll=0)


plt.plot(t, E, color='blue')
plt.title('$E^*(t)$ (tercer caso)')
plt.xlabel('$t$')
plt.ylabel('$E^*$')

plt.legend()
plt.savefig('code/e3.pdf')

plt.show()