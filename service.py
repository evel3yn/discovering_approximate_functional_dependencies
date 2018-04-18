# -*- coding: utf-8 -*-
"""
Data Mining Programming Assignment

This script aims to discover approximate functional dependencies in a given 
data set.
"""
import sys


def pprint(FDs):
    """Pretty print of discovered FDs
    """
    print('\nDiscovered FDs:')
    for fd in FDs:
        print(', '.join(fd[0]), " -> ", fd[1], ' with support ', fd[2])


def load_data(filename):
    """Read data from data_file_name and return a list of lists, 
    where the first list (in the larger list) is the list of attribute names, 
    and the remaining lists correspond to the tuples (rows) in the file.
    """
    with open(filename, 'rU') as f:
        results = [[x.rstrip() for x in line.split(',')] for line in f]
    return results


def find_approximate_functional_dependencies(data_file_name, depth_limit, minimum_support):
    """Main function which you need to implement!

    The function discovers approximate functional dependencies in a given data

    Input:
        data_file_name - name of a CSV file with data 
        depth_limit - integer that limits the depth of search through the space of 
            domains of functional dependencies
        minimum_support - threshold for identifying adequately approximate FDs

    Output:
        FDs - a list of tuples. Each tuple represents a discovered FD.
        The first element of each tuple is a list containing LHS of discovered FD
        The second element of the tuple is a single attribute name, which is RHS of that FD
        The third element of the tuple is support for that FD

    Output example:
        [([A],C, 0.91), ([C, F],E, 0.97), ([A,B,C],D, 0.98), ([A, G, H],F, 0.92)]
        The above list represent the following FDs:
            A -> C, with support 0.91
            C, F -> E, with support 0.97 
            A, B, C -> D, with support 0.98
            A, G, H -> F, with support 0.92                   
    """
    # read input data:
    input_data = load_data(data_file_name)

    # Transform input_data (list of lists) into some better representation.
    # You need to decide what that representation should be.
    # Data transformation is optional!
    FDs = []
    topic = input_data[0]
    # waiting queue is a queue for bfs
    waiting_queue = []
    for i in topic:
        waiting_queue.append([i])
    # when k = 1, we need to know the rank of the range1
    rank_solo = 0
    while len(waiting_queue) > 0:
        t = waiting_queue.pop(0)
        # traverse all of the elements in the waiting queue
        # checking
        if len(t) == 1:
            # k = 1
            # key is range1, value is times it shows up
            d_solo = {}
            for data in input_data[1:]:
                data_solo = data[rank_solo]
                if d_solo.get(data_solo) is None:
                    d_solo[data_solo] = 1
                else:
                    d_solo[data_solo] = d_solo.get(data_solo) + 1
            # the sum of max value of times the range1 shows up, for each domain
            max_solo = 0
            # total times of the range1 shows up, for all of the domain
            all_solo = 0
            for k, v in d_solo.items():
                if v > max_solo:
                    max_solo = v
                all_solo += v
            sup_solo = max_solo / all_solo
            if sup_solo > minimum_support:
                t_solo = ([], t[0], sup_solo)
                FDs.append(t_solo)

            rank_solo += 1

        else:
            lenthk = len(t)
            domain = []
            range1 = []
            for i in range(0, len(t)):
                if i != len(t) - 1:
                    domain.append(t[i])
                else:
                    range1.append(t[i])
            # find the times domain and range show up
            # set up a dictionary to store the show up times
            # the key of d is domain and range, the value is times
            d = {}
            for data1 in input_data[1:]:
                data = tuple(data1[0:lenthk])
                if d.get(data) is None:
                    # d doesn't have value data
                    d[data] = 1
                else:
                    d[data] = d.get(data) + 1
            # traverse the dictionary to count
            # in dictionary d2, key is domain, value is [[range1,times],[]]
            d2 = {}
            for doran, num in d.items():
                do = tuple(doran[0:len(doran) - 1])
                ran = [doran[-1]]
                if d2.get(do) is None:
                    d2[do] = [[ran, 1]]
                else:
                    v = d2.get(do)
                    # is there already a range item in this domain
                    exitsflag = False
                    for i in v:
                        if i[0] == ran:
                            # exists
                            i[1] += 1
                            exitsflag = True
                    if exitsflag is False:
                        v.append([ran, 1])
            # compute the support number
            element = 0
            denomina = 0
            for k, v in d2.items():
                # the sum of max value of times the range1 shows up, for each domain
                max1 = 0
                # total times of the range1 shows up, for all of the domain
                all1 = 0
                for i in v:
                    if i[-1] > max1:
                        max1 = i[-1]
                    all1 += i[-1]
                element += max1
                denomina += all1
            # the support number
            sup = element / denomina
            if sup > minimum_support:
                ttt = (domain, range1[0], sup)
                FDs.append(ttt)

        # put the child of A in the end of the queue
        flag = False
        permit1 = False
        last_element = t[-1]
        if len(t) < depth_limit:
            # we will let it add child
            permit1 = True
        for e in topic:
            if last_element == e:
                flag = True
            if flag is True and permit1 is True and last_element != e:
                waiting_queue.append(t + [e])

    # --------Your code here! Optional! ----------#

    # Discover FDs with given minimun support and depth limit:

    # --------Your code here!---------------------#

    return FDs


if __name__ == '__main__':
    # parse command line arguments:
    # if len(sys.argv) < 3:
    #     print('Wrong number of arguments. Correct example:')
    #     print('python find_fds.py input_data_set.csv 3 0.91')
    # else:
    # data_file_name = str(sys.argv[1])
    # depth_limit = int(sys.argv[2])
    # minimum_support = float(sys.argv[3])
    data_file_name = "SimpleSampleDB.txt"
    depth_limit = 3
    minimum_support = 0.9

    # Main function which you need to implement.
    # It discover FDs in the input data with given minimum support and depth limit
    FDs = find_approximate_functional_dependencies(data_file_name, depth_limit, minimum_support)

    # print you findings:
    pprint(FDs)
