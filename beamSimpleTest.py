from src import Functions, Beam

data = [ ['age', 'married', 'own house', 'income', 'gender', 'class'],
[22, False,False, 20000, 'male, ',False],
[46, False,True,  20000, 'male, ',False],
[24, True, True,  20000, 'male, ',False],
[25, False,False, 20000, 'male, ',False],
[29, True, True,  20000, 'male, ',False],
[45, True, True,  20000, 'male, ',True],
[63, True, True,  21000, 'female',True],
[36, True, False, 30000, 'female',True],
[23, False,True,  40000, 'female',True],
[50, True, True,  55000, 'female',True]
]

types = ['nominal', 'binary', 'binary', 'numeric', 'nominal', 'binary']

target = ['class']

phi = Functions.WARcc

res = Beam.beam_algorithm(data, phi, Beam.refinement, 4, 3, 4, 3, set(), target, types)

if __name__ == '__main__':

    Functions.representSolution(res, data[0])