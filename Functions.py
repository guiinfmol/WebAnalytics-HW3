import math

def yuleQualityMeasure(dataset, subgroup, targets):


    subgroup_comp = [i for i in dataset if i not in subgroup]
    yuleQsub = yuleQ(subgroup, targets)
    yuleQsub_comp = yuleQ(subgroup_comp, targets)

    yule = math.fabs(yuleQsub - yuleQsub_comp)

    return yule * entropy(len(subgroup), len(dataset))


def yuleQ(s, targets):

    target1 = targets[0]
    target2 = targets[1]

    n1 = len([i for i in s if i[target1]])
    n2 = len([i for i in s if not i[target1]])
    n3 = len([i for i in s if i[target2]])
    n4 = len([i for i in s if not i[target2]])

    return ((n1*n4) - (n2*n3))/(n1+n2+n3+n3)


def entropy(subgroup_size, total_size):

    n = subgroup_size
    n_comp = total_size - subgroup_size
    log1 = math.log(n, math.e)
    log2 = math.log(n_comp, math.e)

    res = -(n/total_size * log1) - (n_comp/total_size * log2)

    return res


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