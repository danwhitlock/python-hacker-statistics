import numpy as np
import matplotlib.pyplot as plt

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
        step = max(0, step - 1) # use max to make sure step can't go below 0
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)
    
    random_walk.append(step)

# print out the new step value
print(random_walk)

# Plot the random walk using matplotlib.pyplot
plt.plot(random_walk)
plt.title("Simulation")
plt.xlabel("Roll")
plt.ylabel("Step")

# display the plot
plt.show()