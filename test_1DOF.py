import SingleDOF as SDOF


sys = SDOF.system(mass=1, stiffness=1, damping=0.1,position=5, velocity=1)

sys.plot_response(100, 10000)