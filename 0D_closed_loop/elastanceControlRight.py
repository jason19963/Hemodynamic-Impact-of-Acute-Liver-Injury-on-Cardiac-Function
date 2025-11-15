from CRIMSONPython import *
from math import pi, cos
import numpy


class parameterController(abstractParameterController):

    def __init__(self, baseNameOfThisScriptAndOfRelatedFlowOrPressureDatFile, MPIRank):
        abstractParameterController.__init__(self, baseNameOfThisScriptAndOfRelatedFlowOrPressureDatFile, MPIRank)
        # self.m_baseNameOfThisScript = baseNameOfThisScriptAndOfRelatedFlowOrPressureDatFile
        self.periodicTime = 0;
        self.stepIndex = 0

        # elastance parameters
        self.m_timeToMaximumElastance = 0.3765742748415696
        self.m_timeToRelax = 0.10419963555027723
        self.m_minimumElastance = 9.33865711399183e-05
        self.m_maximumElastance = 0.1520309478

        self.elastance_history = numpy.array([])

        # hemodynamic metrics
        self.m_heartPeriod = 0.684022021679136;

        self.finishSetup()

    def updateControl(self, currentParameterValue, delt, dictionaryOfPressuresByNodeIndex,
                      dictionaryOfFlowsByComponentIndex, dictionaryOfVolumesByComponentIndex):

        self.stepIndex += 1

        # retrieving timeStep and elastance values
        self.updatePeriodicTime(delt)
        elastance = self.getElastance(currentParameterValue)

        self.elastance_history = numpy.append(self.elastance_history, elastance)

        # writing files
        if self.stepIndex % 50 == 0:
            numpy.savetxt('elastance_history.dat', self.elastance_history)

        return elastance

    def updatePeriodicTime(self, delt):

        self.periodicTime = self.periodicTime + delt
        # Keep periodicTime in the range [0,heartPeriod):
        if self.periodicTime >= self.m_heartPeriod:
            self.periodicTime = self.periodicTime - self.m_heartPeriod

    def getElastance(self, currentParameterValue):
        # *** analytical elastance function from:
        #     pope, s. r.; ellwein, l. m.; zapata, c. l.; novak, v.; kelley, c. t. & olufsen, m. s.
        #     estimation and identification of parameters in a lumped cerebrovascular model.
        #     math biosci eng, 2009, 6, 93-115

        # This is the elastance function. It's defined piecewise:
        if self.periodicTime <= self.m_timeToMaximumElastance:
            elastance = (self.m_minimumElastance \
                        + 0.5 * (self.m_maximumElastance - self.m_minimumElastance) \
                        * (1.0 - cos((self.periodicTime * pi) / self.m_timeToMaximumElastance)))

        elif self.periodicTime <= (self.m_timeToMaximumElastance + self.m_timeToRelax):
            elastance = (self.m_minimumElastance \
                        + 0.5 * (self.m_maximumElastance - self.m_minimumElastance) \
                        * (1.0 + cos((self.periodicTime - self.m_timeToMaximumElastance) * (pi / self.m_timeToRelax))))

        elif self.periodicTime > (self.m_timeToMaximumElastance + self.m_timeToRelax):
            elastance = (self.m_minimumElastance)

        return elastance;

