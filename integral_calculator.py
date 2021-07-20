import math

def main():
  interval = (0, 2);
  # interval[0] & interval[1] are a & b respectively
  is_pi = 0;
  # generated by script

  average_value = get_average_value(interval);
  left_interval, right_interval = integral_function(interval);
  evaluation, is_pi = evaluate(average_value, interval, left_interval, right_interval, is_pi);

  if is_pi == 1:
    print('The average value is: {0}/pi'.format(int(evaluation)));
  else:
    print('The average value is: {0}'.format(int(evaluation)));


def integral_function(interval):
  # use antiderivative
  left_interval = math.ceil((8 * interval[0]) - (3 * (interval[0] ** 2)));
  print('Left: {0}'.format(left_interval));
  right_interval = math.ceil((8 * interval[1]) - (3 * (interval[1] ** 2)));
  print('Right: {0}'.format(right_interval));

  return left_interval, right_interval;

def get_average_value(interval):
  average_value = (1 / (interval[1] - interval[0]));

  return average_value;


def evaluate(average_value, interval, left_interval, right_interval, is_pi):
  evaluation = (average_value * (right_interval - left_interval));

  if evaluation > int(evaluation):
    # if evaluation != int, basically;
    evaluation *= math.pi;
    is_pi = 1;


  return evaluation, is_pi;


main()

## EOF
