from boltons import queueutils as qu

def confusion_matrix(dataset, s, target):
    assert isinstance(dataset, list)
    dt = dataset[:]
    subgroup = [dataset[i] for i in s]
    dt = [i for i in dt if i not in subgroup]

    total = len(dataset)

    positive_target_dt = len([i for i in dt if i[target]]) / total
    negative_target_dt = len([i for i in dt if not i[target]]) / total
    positive_target_subgroup = len([i for i in subgroup if i[target]]) / total
    negative_target_subgroup = len([i for i in subgroup if not i[target]]) / total

    return [[positive_target_subgroup, negative_target_subgroup],[positive_target_dt, negative_target_dt]]

def WARcc(dataset, subgroup, target):
    cf = confusion_matrix(dataset, subgroup, target)

    return cf[0][0] - (cf[0][0] + cf[0][1]) * (cf[0][0] + cf[1][0])


if __name__ == '__main__':

    test_dataset = [[0, 22, False, False, 28000, 'male', False],
                    [1, 22, False, True, 32000, 'female', False],
                    [2, 22, True, True, 24000, 'male', False],
                    [3, 22, False, False, 27000, 'male', False],
                    [4, 22, True, True, 32000, 'female', False],
                    [5, 22, True, True, 30000, 'female', True],
                    [6, 22, True, True, 58000, 'male', True],
                    [7, 22, True, False, 52000, 'male', True],
                    [8, 22, False, True, 40000, 'female', True],
                    [9, 22, True, True, 28000, 'female', True]]

    cf = confusion_matrix(test_dataset, [2, 4, 6, 1], 6)
    war = WARcc(test_dataset, [2, 4, 6, 1], 6)

    #print(cf)
    #print(war)

    a = [3,4,5]

    [a.remove(i) for i in [3,4]]

    print((a))






