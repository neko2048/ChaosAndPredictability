import numpy as np
from scipy.integrate import ode
class Lorenz96:
    def __init__(self, initValues, force):
        self.initValues = initValues
        self.force = force

    def forceODE(self, time, x):
        return (np.roll(x, -1) - np.roll(x, 2)) * np.roll(x, 1) - x + self.force

    def getODESolver(self, initTime=0., solve_method='dopri5', Nstep=10000):
        if Nstep:
            solver = ode(self.forceODE).set_integrator(name=solve_method, nsteps=Nstep)
        else:
            solver = ode(self.forceODE).set_integrator(name=solve_method)
        solver.set_initial_value(self.initValues, t=initTime)#.set_f_params(self.force)
        return solver

    def solveODE(self, endTime):
        self.solver.integrate(endTime)
        xSolution = np.array(self.solver.y, dtype="f8")
        return xSolution