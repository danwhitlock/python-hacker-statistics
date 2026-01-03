import numpy as np
import matplotlib.pyplot as plt


# Python script to calculate the probability of reaching at least step 60 after 100 rolls of a dice
# Start on step 0.  Roll dice and move up or down based on the dice value (1-2: down 1 step, 3-5: up 1 step, 6: roll again and go up that number of steps)
# Include clumsiness factor (there is a 0.5% chance of falling to step 0 on each roll)

# Starting step
step = 0

# Set the seed for random number generator for reproducibility.  Comment out to get different results each time
np.random.seed(123)

# clear the plot in case running multiple times
plt.clf()

# initialise all walks
all_walks = []

for i in range(500):
    random_walk = [0]
    # Control the steps gained/lost based upon the dice value, after 100 rolls
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2 :
            step = max(0, step - 1) # use max to make sure the current step can't go below 0
        elif dice <= 5 :
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
        
        # Implement a clumsiness factor - overall 0.5% chance of falling to step 0
        if np.random.rand() <= 0.005 :
            step = 0
        
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to a NumPy array & transpose
np_aw_t = np.transpose(np.array(all_walks))

# capture final/end positions
ends = np_aw_t[-1,:]

# Confirm the probability that you'll reach at least step 60 
probability = np.mean(ends >= 60)
print("Probability of reaching at least step 60 is: " + str(probability*100) + "%")

# Plot all walks & show
plt.hist(ends)
plt.title("Distribution: 500 Random Walks of 100 Steps Each")
plt.xlabel("Roll Number")
plt.ylabel("Position")
plt.show()