import SingleDOF as SDOF


sys = SDOF.system(mass=1, stiffness=10, damping=1)

sys.plot_response(1000, 10000)