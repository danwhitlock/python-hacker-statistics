import numpy as np
import matplotlib.pyplot as plt

# Starting step
step = 0

# Set the seed
np.random.seed(123)

# initialise all walks
all_walks = []

for i in range(5):
    random_walk = [0]
    # Control the steps gained/lost based upon the dice value, after 100 rolls
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2 :
            step = max(0, step - 1) # use max to make sure step can't go below 0
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
        
        random_walk.append(step)
    
    all_walks.append(random_walk)

# Convert all_walks to a NumPy array
np_aw = np.array(all_walks)

# transpose np_aw in order to visualise five random walks
np_aw_t = np.transpose(np_aw)

# Plot all walks & show
plt.plot(np_aw_t)
plt.show()