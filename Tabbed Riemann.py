def main():
    interval = (0,5)
    fx = [3, 5, 11, 12, 24, 36, 22, 15, 8, 4, 1]
    n = 10
    # changed by user
    x_interval = [x for x in range(interval[0], interval[1]+1)]
    x_interval_float = []
    x_interval_float_exact = []
    left_x_interval = []
    right_x_interval = []
    left_sums = []
    right_sums = []
    left_sum = 0
    right_sum = 0
    width = ((interval[1] - interval[0]) / n)


    # generated through script
    x_interval, left_x_interval, right_x_interval = interval_calc(x_interval, x_interval_float, x_interval_float_exact, left_x_interval, right_x_interval)
    print('x Interval - {0}'.format(x_interval))
    print('Left x Interval - {0}'.format(left_x_interval))
    print('Right x Interval - {0}'.format(right_x_interval))

    left_sum, right_sum = compute_sums(left_x_interval, right_x_interval, width, left_sum, right_sum, fx)
    print('Left Sum - {0}'.format(left_sum))
    print('Right Sum - {0}'.format(right_sum))




def interval_calc(x_interval, x_interval_float, x_interval_float_exact, left_x_interval, right_x_interval):
    for i in range(len(x_interval)):
        # finds the average interval for each val in x_interval
        try: 
            x_interval_float.append((x_interval[i] + x_interval[i+1]) / 2)
        except:
            continue
    
    x_interval = x_interval + x_interval_float
    x_interval.sort()

    for i in range(len(x_interval_float)):
        # re-averages tuple values in interval_a
        try:
            x_interval_float_exact.append((x_interval_float[i] + x_interval_float[i+1]) / 2)
        except:
            continue

    left_x_interval = [x for x in x_interval[:-1]]
    right_x_interval = [x for x in x_interval[1:]]

    return x_interval, left_x_interval, right_x_interval
    



def compute_sums(left_x_interval, right_x_interval, width, left_sum, right_sum, fx):
    for i in range(len(left_x_interval)):
        left_sum += fx[i] * width

    for i in range(len(right_x_interval)):
        right_sum += fx[i+1] * width


    return left_sum, right_sum



main()

## EOF
