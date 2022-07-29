import itertools, timeit

def my_permutations(iterable):

    perm_list = [[]]
    updater_list = []

    for element in iterable:

        for perm in perm_list:

            # i put the next element in every possible place in all of the arrangements with n elements
            # in order to have all of the different arrangements with n+1 elements
            for idx in range(len(perm)):
                # the obj being iterated shouldn't be mutated
                temp_perm = perm.copy()
                temp_perm.insert(index, element)
                updater_list.append(temp_perm)

        # the obj being iterated shouldn't be mutated
        perm_list = updater_list.copy()
        updater_list = []

    return perm_list

# comparison with itertools.permutations
time1 = timeit.timeit("my_permutations(range(20))", "from __main__ import my_permutations", number=10000)
time2 = timeit.timeit("permutations(range(20))", "from itertools import permutations", number=10000)
print("my_permutations' score: ", time1, "\nItertools.permutations' score: ", time2)
print("Itertools.permutations is {ratio} times faster.".format(ratio=time1/time2))

#permutations = my_permutations('ABCD')
#print(len(permutations), "permutations:")
#for i in permutations:
#    print(i)
