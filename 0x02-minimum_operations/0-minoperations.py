#!/usr/bin/python3
'''The minimum operations coding challenge using python.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations required.

    '''
    if not isinstance(n, int):
        return 0
    no_of_ops = 0
    clipboard = 0
    done = 1
    # print('H', end='')
    while done < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = done
            done += clipboard
            no_of_ops += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            no_of_ops += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            no_of_ops += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return no_of_ops
