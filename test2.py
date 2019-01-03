import csv
import Beam
import Functions

file = open('data/sample.csv')
a = csv.reader(file, dialect='excel-tab')

data = []

for i in a:
    data.append(i[:19])

types = ['nominal' for _ in range(0, 20)]

types[9] = 'binary'
types[10] = 'binary'


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

    omega = data
    phi = Functions.yuleQualityMeasure
    eta = Beam.refinement
    w = 2
    d = 2
    b = 4
    q = 4
    c = set()
    targets = ['Combination Id','Converted']

    res = Beam.beam_algorithm(omega, phi,eta, w, d, b, q, c, targets, types)

    while res:
        print(res.pop())