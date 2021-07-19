import math

def main():
  interval = ((-math.pi/2), (math.pi/2));
  # interval[0] & interval[1] are a & b respectively
  # generated by script

  average_value = get_average_value(interval);
  left_interval, right_interval = integral_function(interval);
  evaluation = evaluate(average_value, interval, left_interval, right_interval);

  print('The average value is - {0}/pi'.format(int(evaluation)));


def integral_function(interval):
  left_interval = math.ceil((11 * math.cos(interval[1])));
  right_interval = math.ceil((11 * math.cos(interval[0])));

  return left_interval, right_interval;

def get_average_value(interval):
  average_value = (1 / (interval[1] - interval[0]));

  return average_value;


def evaluate(average_value, interval, left_interval, right_interval):
  evaluation = (average_value * (right_interval - left_interval));

  evaluation *= math.pi;

  return evaluation;


main()

## EOF