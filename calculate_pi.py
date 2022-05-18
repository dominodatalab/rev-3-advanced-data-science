import time

import math
import random
import time

def sample(num_samples):
    num_inside = 0
    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.hypot(x, y) <= 1:
            num_inside += 1
    return num_inside

def approximate_pi(num_samples):
    start = time.time()
    num_inside = sample(num_samples)
    end = time.time()
    
    print("pi ~= {}".format((4*num_inside)/num_samples))
    print('total time in seconds ', (end - start))


approximate_pi(10**8)