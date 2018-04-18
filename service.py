# -*- coding: utf-8 -*-
"""
Data Mining Programming Assignment

This script aims to discover approximate functional dependencies in a given 
data set.
"""
import sys
import Queue


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
    topic = input_data[0]
    waiting_queue = Queue.queue()
    for i in topic
        wa
    waiting_queue = topic
    for t in topic:
        # traverse all of the elements in the waiting queue
        # checking
        # put the child of A in the end of the queue
        waiting_queue.

    # --------Your code here! Optional! ----------#

    # Discover FDs with given minimun support and depth limit:
    FDs = []

    # --------Your code here!---------------------#

    return FDs


if __name__ == '__main__':
    # parse command line arguments:
    if len(sys.argv) < 3:
        print('Wrong number of arguments. Correct example:')
        print('python find_fds.py input_data_set.csv 3 0.91')
    else:
        data_file_name = str(sys.argv[1])
        depth_limit = int(sys.argv[2])
        minimum_support = float(sys.argv[3])

        # Main function which you need to implement.
        # It discover FDs in the input data with given minimum support and depth limit
        FDs = find_approximate_functional_dependencies(data_file_name, depth_limit, minimum_support)

        # print you findings:
        pprint(FDs)
