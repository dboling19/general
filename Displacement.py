def main():
    # Displacement of an object calculator
    # Author Daniel Boling - 2021

    interval = (1, 5)
    # formatted as a tuple
    factor = 4
    # inputted by the user
    rough_velocity = []
    exact_velocity = []
    rough_displacement = 0
    exact_displacement = 0
    rough_displacement_temp = []
    exact_displacement_temp = []
    temp_interval = []
    interval_a = []
    interval_b = []
    # filled in by the script

    interval_calc(interval, temp_interval, interval_a, interval_b)
    velocity(interval_a, interval_b, factor, rough_velocity, exact_velocity)
    print('Rough Velocity - {0}'.format(rough_velocity))
    print('Exact Velocity - {0}'.format(exact_velocity))
    displacement(interval_a, interval_b, rough_velocity, exact_velocity, rough_displacement, exact_displacement, rough_displacement_temp, exact_displacement_temp)


def interval_calc(interval, temp_interval, interval_a, interval_b):
    temp_interval = [x for x in range(interval[0], interval[1]+1)]
    # populates a table of values from a to b

    for i in range(len(temp_interval)):
        # finds the average interval for each val in temp_interval
        try: 
            interval_a.append((temp_interval[i] + temp_interval[i+1]) / 2)
        except:
            continue
    
    temp_interval_a = temp_interval + interval_a
    temp_interval_a.sort()

    for i in range(len(temp_interval_a)):
        # re-averages tuple values in interval_a
        try:
            interval_b.append((temp_interval_a[i] + temp_interval_a[i+1]) / 2)
        except:
            continue

    return interval_a, interval_b


def velocity(interval_a, interval_b, factor, rough_velocity, exact_velocity):
    # finds rough velocity using values in table
    for i in interval_a:
        rough_velocity.append((4 * (i**2)) + factor)

    # finds exact velocity using values in table
    for i in interval_b:
        exact_velocity.append((4 * (i**2)) + factor)

    return rough_velocity, exact_velocity

def displacement(interval_a, interval_b, rough_velocity, exact_velocity, rough_displacement, exact_displacement, rough_displacement_temp, exact_displacement_temp):
    time = interval_a[1] - interval_a[0]
    for i in rough_velocity:
        rough_displacement_temp.append(i * time)
        
    for i in rough_displacement_temp:
        rough_displacement += i
        
    time = interval_b[1] - interval_b[0]
    for i in exact_velocity:
        exact_displacement_temp.append(i * time)
    
    for i in exact_displacement_temp:
        exact_displacement += i

    print('Rough Displacement - {0}'.format(rough_displacement))
    print('Exact Displacement - {0}'.format(exact_displacement))


main()

## EOF
