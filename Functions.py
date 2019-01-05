import math
import csv
from datetime import datetime
import time
import Beam
import PriorityQ as pq

def yuleQualityMeasure(dataset, subgroup, targets):

    subgroup_comp = [i for i in dataset if i not in subgroup]
    yuleQsub = yuleQ(subgroup, targets, dataset)
    yuleQsub_comp = yuleQ(subgroup_comp, targets, dataset)

    yule = math.fabs(yuleQsub - yuleQsub_comp)

    return yule * entropy(len(subgroup), len(dataset))


def yuleQ(s, targets, dataset):

    target1 = targets[0]
    target2 = targets[1]

    all_val_targ1 = set([a[target1] for a in dataset])
    all_val_targ2 = set([a[target2] for a in dataset])

    target1val1 = all_val_targ1.pop()
    target1val2 = all_val_targ1.pop()

    target2val1 = all_val_targ2.pop()
    target2val2 = all_val_targ2.pop()

    n1 = len([i for i in s if i[target1] == target1val1])
    n2 = len([i for i in s if i[target1] == target1val2])
    n3 = len([i for i in s if i[target2] == target2val1])
    n4 = len([i for i in s if not i[target2] == target2val2])

    if ((n1*n4)+(n1*n3)) == 0:
        res = 0.
    else:
        res = ((n1 * n4) - (n2 * n3)) / ((n1 * n4) + (n1 * n3))
    return res


def entropy(subgroup_size, total_size):

    n = subgroup_size
    n_comp = total_size - subgroup_size
    log1 = math.log(n/total_size, math.e)
    log2 = math.log(n_comp/total_size, math.e)

    res = -(n/total_size * log1) - (n_comp/total_size * log2)

    return res


def confusion_matrix(dataset, s, target):
    assert isinstance(dataset, list)
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


def dataPreProcessing(file, features, targets):
    file = open(file, encoding='latin-1')
    a = csv.reader(file, dialect='excel-tab')

    data = []
    types = []
    for i in a:
        data.append(i)
        break

    for i in a:

        if len(i) < len(data[0]):
            aux = i[:] + [0, 0]
        else:
            aux = i[:]
        if aux[9] == 1:
            aux[9] = True
        if aux[9] == 2:
            aux[9] = False
        if aux[10] == 'Yes':
            aux[10] = True
        if aux[10] == 'No':
            aux[10] = False
        if aux[12] == 'TRUE':
            aux[12] = True
        if aux[12] == 'FALSE':
            aux[12] = False
        hit_dt = aux[13]
        dt = datetime.strptime(hit_dt, '%Y-%m-%dT%H:%M:%S')
        dt = time.mktime(dt.timetuple())
        aux[13] = dt
        data.append(aux)

    types = ['nominal' for _ in range(0, 22)]
    types[9] = 'binary'
    types[10] = 'binary'
    #types[11] = 'numeric'
    types[12] = 'binary'
    types[13] = 'numeric'

    all_features = data[0]
    if features != 'all':
        all_features = [i for i in all_features if i in features or i in targets]

    list_of_indices = [i for i in range(0, len(data[0])) if data[0][i] in all_features]

    final_data = []

    for item in data:
        item = [item[i] for i in range(0, len(item)) if i in list_of_indices]
        final_data.append(item)

    types = [types[i] for i in range(0, len(types)) if i in list_of_indices]

    for i in final_data:
        if not len(i) == 9:
            final_data.remove(i)

    return final_data, types

def representSolution(sol, names):
    assert isinstance(sol, pq.PriorityQ)

    for item in sol.dict_tuple_priority.keys():
        quality = sol.dict_tuple_priority.get(item)
        res = ""
        for i in item:
            res+=str(names[i[0]]) +" "+ representFunction(i[2]) + " " + str(i[1]) + "| "
        res+="quality = "+str(quality)
        print(res)

def representFunction(func):
    if func == Beam.eq:
        return "="
    if func == Beam.neq:
        return "!="
    if func == Beam.gteq:
        return ">="
    if func == Beam.leeq:
        return "<="


def printList(lista):
    for i in lista:
        print(i)
