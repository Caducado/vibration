import numpy as np  


class system():
    def __init__(self, mass, stiffness, damping=.0, position=.0, velocity=.0) -> None:
        self.gravity = 9.8069
        self.mass = mass
        self.siffness = stiffness
        self.damping = damping
        self.x_0 = position
        self.v_0 = velocity
        self.forces = []
        self.omega_n = np.sqrt(self.siffness/self.mass)
    

  
    