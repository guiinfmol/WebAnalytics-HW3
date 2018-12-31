from boltons import queueutils as qu
import Beam

# FUNCTIONAL DEMO

def confusion_matrix(dataset, s, target):
    assert isinstance(dataset, list)
    target = dataset[0].index(target)
    dt = dataset[:]
    #subgroup = [dataset[i] for i in s]
    subgroup = s
    dt = [i for i in dt if i not in subgroup]

    total = len(dataset)

    positive_target_dt = len([i for i in dt if i[target]]) / total
    negative_target_dt = len([i for i in dt if not i[target]]) / total
    positive_target_subgroup = len([i for i in subgroup if i[target]]) / total
    negative_target_subgroup = len([i for i in subgroup if not i[target]]) / total

    return [[positive_target_subgroup, negative_target_subgroup],[positive_target_dt, negative_target_dt]]

def WARcc(dataset, subgroup, target):
    cf = confusion_matrix(dataset, subgroup, target[0])

    return cf[0][0] - (cf[0][0] + cf[0][1]) * (cf[0][0] + cf[1][0])



if __name__ == '__main__':

    types = ['numeric', 'binary', 'binary', 'numeric', 'nominal', 'binary']
    targets = ['class']
    test_dataset = [['age', 'married', 'own house', 'income', 'gender', 'class'],
                    [22, False, False, 28000, 'male', False],
                    [46, False, True, 32000, 'female', False],
                    [24, True, True, 24000, 'male', False],
                    [25, False, False, 27000, 'male', False],
                    [29, True, True, 32000, 'female', False],
                    [45, True, True, 30000, 'female', True],
                    [63, True, True, 58000, 'male', True],
                    [36, True, False, 52000, 'male', True],
                    [23, False, True, 40000, 'female', True],
                    [50, True, True, 28000, 'female', True]]

    refinement = Beam.refinement
    quality_mes = WARcc

    '''
    (omega,               # Dataset
    phi,                 # Quality measure
    eta,                 # Refinement operator
    w,                   # Beam width
    d,                   # Beam depth
    b,                   # Numbers of bins n
    q,                   # Result set size q
    c,                   # Constraints set c
    targets,             # Names of the features treated as targets
    types): 
    '''
    res = Beam.beam_algorithm(test_dataset, quality_mes, refinement, 3, 3, 4, 5, set(), targets, types)
    print("TOP q descriptions are:")
    print("-----------------------")
    while res:
        desc = res.pop()
        s = Beam.get_subgroup(desc, test_dataset)
        qual = WARcc(test_dataset, s, targets)
        print(desc)
        print(qual)
        print("-----------------------")










