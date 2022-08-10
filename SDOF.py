import numpy as np 
import matplotlib.pyplot as plt
import logging




logging.basicConfig(level=logging.INFO)
class system():
    def __init__(self, mass, stiffness, damping=.0, position=1, velocity=.0) -> None:
        self.gravity = 9.8069
        self.m = mass
        self.k = stiffness
        self.c= damping
        self.x_0 = position
        self.v_0 = velocity
        self.forces = []
        self.w_n = np.sqrt(self.k/self.m)
        self.f_n = np.sqrt(self.k/self.m)/(2*np.pi)
    
    def response(self, T: float=100.0, N:int=10000) -> float:
        t = np.linspace(0, T, N)
        self.zeta = self.c/(2*self.m*self.w_n)
        logging.info(f'zeta is {self.zeta}')
        if self.zeta == .0:         #não amortecido
            x = self.x_0*np.cos(self.w_n*t) + (self.v_0/self.w_n)*np.sin(self.w_n*t)
        
        elif self.zeta < 1.0:       #subamortecido
            C1 = self.x_0
            C2 = (self.v_0 + self.zeta*self.w_n+self.x_0)/(np.sqrt(1-self.zeta**2)*self.w_n)
            x = np.exp(-self.zeta*self.w_n*t)*(C1*np.cos(np.sqrt(1-self.zeta**2)*self.w_n*t) + C2*np.sin(np.sqrt(1-self.zeta**2)*self.w_n*t))
        elif self.zeta == 1.0:      #criticamente amortecido
            C1 = self.x_0
            C2 = self.v_0 + self.w_n*self.x_0
            x = (C1 + C2*t)*np.exp(-self.w_n*t)            
        else:                       #superamortecido
            C1 = (self.x_0*self.w_n*(self.zeta+np.exp(-self.zeta+np.sqrt(self.zeta**2-1))+self.v_0))/(2*self.w_n*np.sqrt(self.zeta**2-1))
            C2 = (-self.x_0*self.w_n*(self.zeta-np.exp(-self.zeta+np.sqrt(self.zeta**2-1))-self.v_0))/(2*self.w_n*np.sqrt(self.zeta**2-1))
            x = C1*np.exp((-self.zeta+np.sqrt(self.zeta**2-1))*self.w_n*t) + C2*np.exp((-self.zeta-np.sqrt(self.zeta**2-1))*self.w_n*t)

                 
        return t, x
    
    def plot_response(self, T: float=100.0, N:int=10000) -> None:
        t, x = self.response(T, N)
        plt.figure()
        plt.plot(t, x)
        plt.show()
        return 
  


 