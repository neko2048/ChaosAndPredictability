import numpy as np
from lorenz96 import Lorenz96

class DataGenerator:
    def __init__(self, nTimeStep, dt):
        self.nTimeStep = nTimeStep
        self.dt = dt

    def setupLorenz96(self, initPerturb, force):
        self.initPerturb = initPerturb
        self.nGrid = len(initPerturb)
        self.force = force
        self.lorenz96 = Lorenz96(self.initPerturb, self.force)
        self.lorenz96.solver = self.lorenz96.getODESolver(Nstep=self.nTimeStep)

    def getSeriesTruth(self):
        xTruth = self.initPerturb # initial truth
        self.lorenz96 = Lorenz96(self.initPerturb, self.force)
        solver = self.lorenz96.getODESolver()
        print(solver)
        nowTimeStep = 1
        while solver.successful() and nowTimeStep <= self.nTimeStep-1: # exclude zero
            solver.integrate(solver.t + self.dt)
            xTruth = np.vstack([xTruth, [solver.y]])
            if nowTimeStep % 50 == 0:
                print("Current TimeStep: {NTS:03d} | Time: {ST}".format(NTS=nowTimeStep, ST=round(solver.t, 5)))
            nowTimeStep += 1
        return xTruth
