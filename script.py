# Import numpy as np
import numpy as np

# Starting step
step = 0

# Set the seed
np.random.seed(123)

# initialise a random walk
random_walk = [0]

# Control the steps gained/lost based upon the dice value, after 100 rolls
for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)
    
    random_walk.append(step)

# print out the new step value
print(random_walk)