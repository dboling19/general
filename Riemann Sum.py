def main():
    interval = (1,5)
    n = 4
    # changed by user
    sums = []
    left_sums = []
    right_sums = []
    left_sum = 0
    right_sum = 0
    left_sub_ints = [x for x in range(interval[0], (interval[1]+1)-1)]
    right_sub_ints = [x for x in range(interval[0]+1, interval[1]+1)]
    width = ((interval[1] - interval[0]) / n)
    # generated through script
    
    print('Left-Sub-Integers - {0}'.format(left_sub_ints))
    print('Right-Sub-Integers - {0}'.format(right_sub_ints))

    for i in left_sub_ints:
        # find left sub integer values
        f(i, left_sums)

    for i in right_sub_ints:
        # find right sub integer values
        f(i, right_sums)

    print('Left Sums - {0}'.format(left_sums))
    print('Right Sums - {0}'.format(right_sums))

    compute_sums(left_sums, right_sums, width, left_sum, right_sum)


    
def f(x, sums):
    # must be changed by user
    sums.append((2/x) + 4)


def compute_sums(left_sums, right_sums, width, left_sum, right_sum):
    for i in left_sums:
        left_sum += i * width

    print('Left Sum - {0}'.format(left_sum))

    for i in right_sums:
        right_sum += i * width

    print('Right Sum - {0}'.format(right_sum))

    return left_sum, right_sum



main()

## EOF
