import numpy as np 
import matplotlib.pyplot as plt


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
    
    def response(self, T: float=100.0, N:int=1000) -> float:
        t = np.linspace(0, T, N)
        if self.c is .0:
            x = self.x_0*np.cos(self.w_n*t) + (self.v_0/self.w_n)*np.sin(self.w_n*t)
        else:
            self.zeta = self.c/(2*self.m*self.w_n)
            if self.zeta > 1.0:
                elif self.zeta == 1.0

        return t, x
    
    def plot_response(self, T: float=100.0, N:int=1000, fig) -> None:
        t, x = self.response(T, N)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(t, x)
        ax.show()
        return fig
  
    