import csv
import Beam
import Functions

data, types = Functions.dataPreProcessing('data/sample2.csv', 'all', ['Converted', 'Combination Id'])

'''In the lines above the work flow is simple: we reed the csv file, we only take the first 19 features, also we create
the 'types' array (needed for the beam algorithm), we declare of all the types as nominal except for the two target 
variables which are binary'''

if __name__ == '__main__':
    '''def beam_algorithm(omega,  # Dataset
                       phi,  # Quality measure
                       eta,  # Refinement operator
                       w,  # Beam width
                       d,  # Beam depth
                       b,  # Numbers of bins n
                       q,  # Result set size q
                       c,  # Constraints set c
                       targets,  # Names of the features treated as targets
                       types): 
    '''

    omega = data  # Sample dataset
    phi = Functions.yuleQualityMeasure
    eta = Beam.refinement
    w = 10
    d = 2
    b = 4
    q = 5
    c = set()
    targets = ['Combination Id','Converted']

    res = Beam.beam_algorithm(omega, phi,eta, w, d, b, q, c, targets, types)


    Functions.representSolution(res, phi, omega, targets)

    while res:
        aux = res.pop()
        sgrp = Beam.get_subgroup(aux, omega)
        quality = 1 #Functions.yuleQualityMeasure(omega, sgrp, )
        print(str(aux) + " " + str(quality))