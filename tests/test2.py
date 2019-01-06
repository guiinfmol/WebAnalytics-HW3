import Beam
import Functions
import csv
from timeit import default_timer as timer


file = open('data/modified6.csv', encoding='latin-1')
a = csv.reader(file, dialect='excel-tab')


data =[]

for i in a:
    data.append(i)


names = data[0]
ind_of = names.index('Returning Visitor')

types = ['nominal' for _ in range(0, len(data[0]))]

types[ind_of] = 'binary'

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

    start = timer()

    res = Beam.beam_algorithm(omega, phi,eta, w, d, b, q, c, targets, types)

    end = timer() - start

    Functions.representSolution(res, omega[0])

    print("Duration of demo: " + str(int(end//60)) + " min and " + str(round(end%60)) + " sec.")
