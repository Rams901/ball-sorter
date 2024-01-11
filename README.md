 # Ball Sorter Problem
 - <b>Description</b> you specify N = number of buckets, and an equal number of balls. Imagine all buckets a placed in a line, numbered from bucket 1 to lets say 4 (N=4). You start with all the 4 balls placed inside a single bucket (could be any one of the 4). And your destination is to distribute all the balls evenly across the buckets- so the end state is one ball per bucket. You can only move one ball from one bucket to the next in each move 
 - <b> Goal</b> the goal is to solve this in the optimal (least) number of total moves.

# Ball Sorter in Reinforcement Learning

BallSorter is a custom gymnasium environment that simulates sorting a given number of balls into equally filled buckets. This operator takes a single action and returns a reward and a new observation based on that action. The environment resets when all balls are sorted, and the goal is to minimize the number of moves required to sort all balls.

Inputs:

The input to this operator is an integer action from the action space. The action is an integer between 0 and 2 that represents moving the ball to the left, right, or no movement.

Parameters:

The operator has no parameters.

Outputs:

The operator returns a tuple containing the new observation, local reward, done flag, info dictionary, and whether the episode is truncated. The new observation is a one-dimensional numpy array that represents the state of the environment. The local reward is a float value between -100 and 100, and the done flag is a boolean indicating whether the episode is complete. The info dictionary is currently empty.

Functionality:

The BallSorter environment has several helper functions supporting its functionality. The `print_debug_info` function prints debug information to the console. The `swap_ball` function swaps the ball at a given position with the ball at the given moved position. The `no_balls_foul` function checks whether there are no balls in a given position and returns a boolean value. The `out_of_bound` function checks whether a given move is within the bounds of the environment and returns a boolean value. The `ball_to_greater_bucket` function checks whether a ball is being moved to a bucket that already has more balls than the current bucket and returns a boolean value. The `filled_balls` function creates an array of filled buckets.

# Agents Used
Using Stable Baseline 3, the approach involved several algorithms used such as PPO, A2C, TRPO.
TRPO was the best model to reach rewarding results in shorter steps.

