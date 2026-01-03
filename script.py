# Import numpy as np
import numpy as np

# Starting step
step = 50

# Set the seed
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1,7)
print("Rolling the dice...")
print("You rolled a " + str(dice))

# Control the steps gained/lost based upon the dice value

if dice <= 2 :
    step = step - 1
elif dice <= 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# print out the new step value
print("You are now on step " + str(step))