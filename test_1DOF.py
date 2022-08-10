import SDOF


sys = SDOF.system(mass=1, stiffness=1, damping=0.1,position=1, velocity=0)

sys.plot_response(100, 10000)

