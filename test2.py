import Beam
import Functions
import csv

# Can be switched
#features = ['Screen Resolution', 'Browser', 'OS', 'Traffic Source', 'Returning Visitor', 'Country', 'User Language']
# feature = 'all'

#data = pandas.read_csv('data/modified.csv', sep = '\t' )
#types = ['Screen Resolution',	'OS',	'Traffic Source',	'Combination Id',	'Converted',	'User Language',	'Country']

#print(data)
# data, types = Functions.dataPreProcessing('data/modified.csv', features, ['Converted', 'Combination Id'])

file = open('data/modified.csv', encoding='latin-1')
a = csv.reader(file, dialect='excel-tab')
data =[]

for i in a:
    data.append(i)



types = ['nominal' for _ in range(0, len(data[0]))]

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
    w = 5
    d = 2
    b = 4
    q = 5
    c = set()
    targets = ['Combination Id','Converted']

    res = Beam.beam_algorithm(omega, phi,eta, w, d, b, q, c, targets, types)


    Functions.representSolution(res, omega[0])

