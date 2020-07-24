from src import Functions, Beam
import csv
from timeit import default_timer as timer

# Here we read the data
file = open('data/final_dataset.csv', encoding='latin-1')
a = csv.reader(file, dialect='excel-tab')

# A little bit of processing of the data. Make data a list as well as removing rows with missing attributes.
data =[]

for i in a:
    data.append(i)

ref_length = len(data[0])

file.close()


print("Analysing ", len(data[1:]), " rows.")

# All features used in the example are nominal, except for returning visitor that is going to be binary (0/1-represented)
names = data[0]
ind_of = names.index('Returning Visitor')

types = ['nominal' for _ in range(0, len(data[0]))]
types[ind_of] = 'binary'

'''In the lines above the work flow is simple: we reed the csv file, also we create
the 'types' array (needed for the beam algorithm), we declare of all the types as nominal except for the two target
variables which are binary'''

if __name__ == '__main__':

    omega = data  # Sample dataset
    phi = Functions.yuleQualityMeasure
    eta = Beam.refinement
    w = 10
    d = 2
    b = 4
    q = 5
    c = set() # We are not using constraints in our example
    targets = ['Combination Id','Converted']

    start = timer()

    res = Beam.beam_algorithm(omega, phi, eta, w, d, b, q, c, targets, types)

    end = timer() - start

    Functions.representSolution(res, omega[0])

    print("Duration of demo: " + str(int(end//60)) + " min and " + str(round(end%60)) + " sec.")
