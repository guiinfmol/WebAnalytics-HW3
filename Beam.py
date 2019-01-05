from collections import deque
import math
import PriorityQ as pq


def beam_algorithm(omega,               # Dataset
                   phi,                 # Quality measure
                   eta,                 # Refinement operator
                   w,                   # Beam width
                   d,                   # Beam depth
                   b,                   # Numbers of bins n
                   q,                   # Result set size q
                   c,                   # Constraints set c
                   targets,             # Names of the features treated as targets
                   types):              # List with the Types of the features in the dataset

    # Pre-treatement of the data. Get the header names.
    names = omega[0]
    target_ind = [names.index(a) for a in targets]  # This is the names of the targets mapped to indices in the names list

    att_indices = list(range(0, len(names)))
    [att_indices.remove(i) for i in target_ind]

    candidate_q = deque([])
    candidate_q.append(())
    result_set = pq.PriorityQ(q)  # This must be a priority queue of size = result_set_size

    # This is an iteration over the N levels provided as parameter depth (d)
    for i in range(0, d):

        # We create the beam as an empty PriorityQueue
        # The size of this beam must be always w at most. This constraint is checked when we add a new item to the
        # queue. That's what insert_with_priority function (defined below) is for. (It was not built-in with the lib)
        beam = pq.PriorityQ(w)  # This is a priority queue of size = w

        # Loop with guard condition 'when candidate_q is not empty then...'
        while bool(candidate_q):

            # Extract a candidate to be refine
            seed = candidate_q.popleft()

            # Here we refine. Eta passed as parameter is a function responsible for the refinement of the seed
            a_set = eta(seed, omega[1:], types, b, att_indices)  # Refinement set... eta [seed]

            # For each description in the refined set
            for desc in a_set:
                # We compute the quality of the description
                sub = get_subgroup(desc, omega[1:])
                #quality = phi(omega[1:], sub, target_ind) I have moved the computation of the quality below

                # If the description meets all the constraints (no constraints applied in our model) and the lenght of
                # the subgroup is > 0. When we compute the quality outside the if{} we cant get divison by zero error.
                if satisfies_all(desc, c) and len(sub)>0: # This way we assure that the subgroups lenght are > 0.
                    quality = phi(omega[1:], sub, target_ind)
                    print(desc)
                    # Then we add this to the beam and the result set with priority quality...
                    result_set.insert_with_piority(tuple(desc), quality)
                    beam.insert_with_piority(tuple(desc), quality)

        while len(beam) != 0:
            element = beam.get_front_element()
            candidate_q.append(element)

    return result_set


# Refinement function as stated in the reference article
def refinement(seed, omega, types, b, att_indices):

    res = []

    used = [i[0] for i in seed]

    cp_att_indices = att_indices[:]

    [cp_att_indices.remove(i) for i in used]

    for i in cp_att_indices:
        aux = list(seed)[:]

        if types[i] == 'numeric':

            s = get_subgroup(seed, omega[1:])
            all_values = [float(entry[i]) for entry in s]

            all_values = sorted(all_values)
            n = len(all_values)
            split_points = [all_values[math.floor(j * (n/b))] for j in range(0, b-1)]

            for s in split_points:
                func1 = leeq
                func2 = gteq
                local0 = aux[:]
                local0.append((i, s, func1))
                local1 = aux[:]

                local1.append((i, s, func2))
                res.append(local0)
                res.append(local1)

        elif types[i] == 'binary':
            func = eq
            local0 = aux[:]
            local0.append((i, 0, func))
            local1 = aux[:]
            local1.append((i, 1, func))
            res.append(local0)
            res.append(local1)
        else:
            # Get all nominal values for this attribute...
            # Here probably instead of using the whole dataset could be more feasible to use just the subgroup!
            all_values = [entry[i] for entry in omega[1:]]
            for j in set(all_values):
                func1 = eq
                func2 = neq
                local0 = aux[:]
                local0.append((i, j, func1))
                local1 = aux[:]
                local1.append((i, j, func2))
                res.append(local0)
                res.append(local1)

    return res


def gteq(a, b):
    return a >= b


def leeq(a, b):
    return a <= b


def eq(a, b):
    return a == b


def neq(a, b):
    return not eq(a, b)


def satisfies_all(desc, c):
    return True


def get_subgroup(description, dataset):
    res = []
    for item in dataset[1:]:
        check = True
        for att in description:
            func = att[2]
            desc_value = att[1]
            att_index = att[0]
            value = func(item[att_index], desc_value)
            if not value:
                check = False
                break
        if check:
            res.append(item)
    return res





