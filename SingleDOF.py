import numpy as np  


class system():
    def __init__(self, mass, stiffness, damping=.0, position=.0, velocity=.0) -> None:
        self.gravity = 9.8069
        self.mass = mass
        self.siffness = stiffness
        self.damping = damping
        self.position = position
        self.velocity = velocity
        self.forces = []
        self.omega_n = np.sqrt(self.siffness/self.mass)
    

  
    def harmonic_load(self, frequency, amplitude):
        self.forces.append(amplitude*np.sin(frequency*self.position))
        return self.forces


    def loads(self, inputs=(.0,.0), gravity_on:bool=True) -> None:
        if gravity_on:
            self.forces.append(-self.mass*self.gravity, .0)
        else:
            self.forces = []
        self.force = inputs
        self.acceleration = inputs / self.mass
        self.velocity += self.acceleration
        self.position += self.velocity
        return self.position
