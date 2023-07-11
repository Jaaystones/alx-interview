#!/usr/bin/python3
'''The minimum operations coding challenge using python.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    no_of_ops = 0
    clipboard = 0
    paste = 1
    # print('H', end='')
    while paste < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = paste
            paste += clipboard
            no_of_ops += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - paste > 0 and (n - paste) % paste == 0:
            # copy all and paste
            clipboard = paste
            paste += clipboard
           no_of_ops += 2
            # print('-(11)->{}'.format('H' * paste), end='')
        elif clipboard > 0:
            # paste
            paste += clipboard
            no_of_ops += 1
            # print('-(01)->{}'.format('H' * paste), end='')
    # print('')
    return no_of_ops
